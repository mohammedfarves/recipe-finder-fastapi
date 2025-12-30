import re
import operator
from typing import Optional
from fastapi import FastAPI, Depends, Query, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
# CRITICAL FIX: Add Text to the imports
from sqlalchemy import or_, and_, func, cast, Float, Text
from sqlalchemy.dialects.postgresql import JSON

# Import your local modules
from .database import get_db
from .models import Recipe
from .schemas import RecipeResponse

app = FastAPI()
origins = [
    "*", # Keep this for development simplicity if you want all origins
    "http://localhost:8000",
    "http://127.0.0.1:8000/static/index.html" # <-- Add this specific origin
]
# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # Use the defined origins list here, not ["*"] again
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Helper to parse filter params (e.g., calories=<=400)
def parse_filter(value: str, field: str):
    if not value:
        return None
    # Updated regex to properly catch operators like <=, >=, !=
    match = re.match(r'^([<>!=]+)(.+)$', value)
    if not match:
        return {'operator': '==', 'val': value, 'field': field}
    operator_str, val = match.groups()
    try:
        val = float(val) if '.' in val or val.isdigit() else val
    except ValueError:
        pass
    return {'operator': operator_str, 'val': val, 'field': field}

@app.get("/")
def read_root():
    return {"message": "API is running. Visit /docs or /static/index.html"}

@app.get("/api/recipes", response_model=dict)
def get_recipes(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    db: Session = Depends(get_db)
):
    offset = (page - 1) * limit
    recipes = db.query(Recipe).order_by(Recipe.rating.desc()).offset(offset).limit(limit).all()
    total = db.query(func.count(Recipe.id)).scalar()
    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": [RecipeResponse.from_orm(r) for r in recipes]
    }

@app.get("/api/recipes/search", response_model=dict)
def search_recipes(
    calories: Optional[str] = None,
    title: Optional[str] = None,
    cuisine: Optional[str] = None,
    total_time: Optional[str] = None,
    rating: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(Recipe)
    filters = []
    
    # Mapping for comparison logic
    ops_map = {
        '<': operator.lt, '<=': operator.le, 
        '>': operator.gt, '>=': operator.ge, 
        '=': operator.eq, '==': operator.eq, '!=': operator.ne
    }

    # 1. Calories Filter (Robust PostgreSQL JSON handling for dirty data)
    if calories:
        cal_filter = parse_filter(calories, 'calories')
        if cal_filter and cal_filter['operator'] in ops_map:
            op_func = ops_map[cal_filter['operator']]
            
            # The most robust FIX for dirty JSON data:
            # a) Extract the value using .astext (works for JSON/JSONB)
            # b) Use func.regexp_replace to strip units like "kcal"
            # c) Use func.nullif to turn any empty strings into SQL NULLs
            # d) Cast the result to Float
            
            cleaned_calories_text = func.regexp_replace(
                Recipe.nutrients['calories'].astext, 
                '[^0-9\.]', '', 'g'
            )
            nullable_calories_text = func.nullif(cleaned_calories_text, '')
            calories_value_as_float = cast(nullable_calories_text, Float)
            
            filters.append(op_func(calories_value_as_float, cal_filter['val']))
    
    # 2. Text Search (Title)
    if title:
        filters.append(Recipe.title.ilike(f"%{title}%"))
    
    # 3. Exact Match (Cuisine)
    if cuisine:
        filters.append(Recipe.cuisine == cuisine)
    
    # 4. Numeric Filters (Total Time & Rating)
    for param_val, param_name in [(total_time, 'total_time'), (rating, 'rating')]:
        if param_val:
            parsed = parse_filter(param_val, param_name)
            if parsed and parsed['operator'] in ops_map:
                op_func = ops_map[parsed['operator']]
                column = getattr(Recipe, param_name)
                filters.append(op_func(column, parsed['val']))
    
    if filters:
        query = query.filter(and_(*filters))
    
    recipes = query.all()
    return {"data": [RecipeResponse.from_orm(r) for r in recipes]}


# Mount static files last
app.mount("/static", StaticFiles(directory="static"), name="static")

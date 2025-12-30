# import json
# import math
# from sqlalchemy.orm import Session
# from project.database import SessionLocal, engine, Base
# from project.models import Recipe

# def create_tables():
#     # Helper function to create tables if they don't exist
#     Base.metadata.create_all(bind=engine)
#     print("Tables ensured.")

# def parse_and_insert():
#     with open('recipes.json', 'r') as f:
#         data = json.load(f)
    
#     db: Session = SessionLocal()
#     # Iterate over the values of the dictionary, not the keys
#     for recipe in data.values(): 
#         # Handle NaN for numeric fields
#         rating = recipe.get('rating')
#         if isinstance(rating, float) and math.isnan(rating):
#             rating = None
#         prep_time = recipe.get('prep_time')
#         if isinstance(prep_time, float) and math.isnan(prep_time):
#             prep_time = None
#         cook_time = recipe.get('cook_time')
#         if isinstance(cook_time, float) and math.isnan(cook_time):
#             cook_time = None
#         total_time = recipe.get('total_time')
#         if isinstance(total_time, float) and math.isnan(total_time):
#             total_time = None
        
#         db_recipe = Recipe(
#             cuisine=recipe['cuisine'],
#             title=recipe['title'],
#             rating=rating,
#             prep_time=prep_time,
#             cook_time=cook_time,
#             total_time=total_time,
#             description=recipe['description'],
#             nutrients=recipe['nutrients'],
#             serves=recipe['serves']
#         )
#         db.add(db_recipe)
#     db.commit()
#     db.close()
#     print("Data inserted")

# if __name__ == "__main__":
#     create_tables() # Create tables before inserting data
#     parse_and_insert()

import json
import math
import re
from sqlalchemy.orm import Session
from project.database import SessionLocal, engine, Base
from project.models import Recipe

def create_tables():
    # Helper function to create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    print("Tables ensured.")

def parse_and_insert():
    with open('recipes.json', 'r') as f:
        data = json.load(f)
    
    db: Session = SessionLocal()
    # Iterate over the values of the dictionary, not the keys
    for recipe in data.values(): 
        # Handle NaN for numeric fields
        rating = recipe.get('rating')
        if isinstance(rating, float) and math.isnan(rating):
            rating = None
        prep_time = recipe.get('prep_time')
        if isinstance(prep_time, float) and math.isnan(prep_time):
            prep_time = None
        cook_time = recipe.get('cook_time')
        if isinstance(cook_time, float) and math.isnan(cook_time):
            cook_time = None
        total_time = recipe.get('total_time')
        if isinstance(total_time, float) and math.isnan(total_time):
            total_time = None


        nutrients = recipe.get('nutrients')

if nutrients and isinstance(nutrients, dict) and isinstance(nutrients.get('calories'), str):
    cleaned_calories = re.sub(r'[^0-9\.]', '', nutrients['calories'])
    try:
        nutrients['calories'] = float(cleaned_calories) if cleaned_calories else None
    except ValueError:
        nutrients['calories'] = None
else:
    nutrients = None



        db_recipe = Recipe(
            cuisine=recipe['cuisine'],
            title=recipe['title'],
            rating=rating,
            prep_time=prep_time,
            cook_time=cook_time,
            total_time=total_time,
            description=recipe['description'],
            nutrients=nutrients, # Insert the cleaned dictionary
            serves=recipe['serves']
        )
        db.add(db_recipe)
    db.commit()
    db.close()
    print("Data inserted")

if __name__ == "__main__":
    create_tables() # Create tables before inserting data
    # NOTE: You must drop your existing 'recipes' table first 
    # to insert the new clean data.
    # Base.metadata.drop_all(bind=engine) 
    parse_and_insert()

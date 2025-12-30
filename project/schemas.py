from pydantic import BaseModel
from typing import Optional, Dict, Any

class RecipeBase(BaseModel):
    # Add Optional[] to all fields that might be missing in your database
    cuisine: Optional[str]
    title: Optional[str] # <-- Was required, now optional
    rating: Optional[float]
    prep_time: Optional[int]
    cook_time: Optional[int]
    total_time: Optional[int]
    description: Optional[str] # <-- Was required, now optional
    nutrients: Optional[Dict[str, Any]] # <-- Was required, now optional
    serves: Optional[str] # <-- Was required, now optional

class RecipeResponse(RecipeBase):
    id: int

    class Config:
        from_attributes = True

from sqlalchemy import Column, Integer, String, Float, Text
# Import the specific PostgreSQL dialect JSONB type
from sqlalchemy.dialects.postgresql import JSONB
    
from .database import Base

class Recipe(Base):
    __tablename__ = "recipes"
    id = Column(Integer, primary_key=True, index=True)
    cuisine = Column(String)
    title = Column(String)
    rating = Column(Float, nullable=True)
    prep_time = Column(Integer, nullable=True)
    cook_time = Column(Integer, nullable=True)
    total_time = Column(Integer, nullable=True)
    description = Column(Text)
    nutrients = Column(JSONB)  # Change JSON to JSONB here
    serves = Column(String)

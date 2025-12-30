**Recipe Finder API & Frontend**

A full-stack application built with FastAPI (Python), PostgreSQL, SQLAlchemy, and a simple HTML/CSS/JavaScript frontend to search and filter recipes.

**Project Structure**
This project is organized into several key files and folders:

/securin task/
    ├── project/
    │   ├── __init__.py         # Makes 'project' a Python package
    │   ├── database.py         # Handles DB connection (PostgreSQL)
    │   ├── models.py           # SQLAlchemy database models
    │   ├── schemas.py          # Pydantic validation schemas
    │   └── main.py             # Main FastAPI application
    ├── static/
    │   ├── index.html          # Frontend HTML structure
    │   ├── styles.css          # Frontend styling
    │   └── script.js           # Frontend JavaScript logic
    ├── insert_recipes.py       # Utility script to populate the database
    ├── recipes.json            # Sample recipe data
    └── README.md               # This documentation file

**Prerequisites**
Before running the application, you need:

Python 3.10+ installed on your system.
PostgreSQL Database Server running on Render use this link for testing --> (postgresql://postgres:12345678@localhost:5432/fastapi_todo).
A virtual environment activated (highly recommended): python -m venv venv and activate it (e.g., .\venv\Scripts\activate on Windows).
Install Dependencies
Install all required Python packages using pip:
bash
pip install fastapi uvicorn pydantic sqlalchemy psycopg2-binary
Use code with caution.

**Installation & Setup**
Follow these steps in order to get the application running:
Step 1: Configure the Database Connection
Open project/database.py.
Replace "your_password" with your actual PostgreSQL password.
python


# project/database.py
DATABASE_URL = "postgresql://postgres:12345678@localhost:5432/fastapi_todo"
# ...
Use code with caution.

Step 2: Create Database Tables
Run the ( insert_recipes.py ) utility script from the root directory (E:\securein\securin task>). This script will automatically ensure the "recipes" table is created and insert the sample data from recipes.json.
bash
# Navigate to the root folder if you aren't already there
cd E:\securein\securin task

# Run the insertion script
python insert_recipes.py
Use code with caution.

You should see:
Tables ensured.
Data inserted
Step 3: Run the FastAPI Server
Start the application using Uvicorn from the root directory (E:\securein\securin task>), ensuring your imports are correctly absolute (from database import ...) and you have an empty __init__.py in the project folder.
bash
python -m uvicorn project.main:app --reload
Use code with caution.

Your terminal should display:
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [...] using StatReload
INFO:     Application startup complete.


**Usage**
Once the server is running on http://127.0.0.1:8000, you can access the following URLs:
Frontend Website
Open your web browser and navigate directly to:
**http://127.0.0.1:8000/docs** for testing api using Swagger ui
**http://127.0.0.1:8000/static/index.html** use this link on browser 
**https://securintask123.onrender.com** This link is Deployed and hosted On Render ( You Can use in Any Devices its mobile Optimized)

This URL loads your HTML, CSS, and JavaScript files via the FastAPI StaticFiles middleware.
API Endpoints (Backend)

**You can also test the API endpoints directly:**
Endpoint	Description
127.0.0.1:8000/docs	*(Interactive API documentation (Swagger UI).*
127.0.0.1:8000	*(List all recipes with pagination.)*
127.0.0.1:8000/static/index.html *(Search recipes using filters (calories, title, rating, etc.))*

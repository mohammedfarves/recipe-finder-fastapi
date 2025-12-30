# 🍲 Recipe Finder API & Frontend

A **full-stack Recipe Finder application** built using **FastAPI**, **PostgreSQL**, and **SQLAlchemy**, with a **responsive HTML/CSS/JavaScript frontend**.

This project allows users to **browse, search, and filter recipes** based on title, calories, rating, and more.
The backend provides REST APIs, while the frontend consumes these APIs and displays data in a clean UI.

🚀 **Live & Deployed on Render (Mobile Optimized)**

---

## 🌐 Live Demo

* 🔗 **Live Application:** [https://securintask123.onrender.com]
* 📘 **Swagger API Docs:** [https://securintask123.onrender.com/docs]
* 🖥 **Frontend UI:** [https://securintask123.onrender.com/static/index.html]

---

## ✨ Features

* 🔍 Search recipes by title
* 🎯 Filter recipes by calories & rating
* 📊 Paginated recipe listing
* ⚡ FastAPI backend with Swagger UI
* 🗄 PostgreSQL database with SQLAlchemy ORM
* 🎨 Clean, responsive frontend (mobile-friendly)
* ☁️ Cloud hosted on Render


## 📁 Project Structure

```
securin task/
│
├── project/
│   ├── __init__.py        # Makes project a Python package
│   ├── database.py        # PostgreSQL DB connection
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   └── main.py            # FastAPI app
│
├── static/
│   ├── index.html         # Frontend HTML
│   ├── styles.css         # Frontend styling
│   └── script.js          # Frontend logic
│
├── insert_recipes.py      # Inserts recipe data
├── recipes.json           # Sample recipe dataset
└── README.md
```

---

## 🧰 Prerequisites

Make sure you have:

* ✅ Python **3.10+**
* ✅ PostgreSQL
* ✅ Virtual environment (recommended)

---

## ⚙ Installation & Setup (Beginner Friendly)

### 🔹 Step 1: Clone the Repository

```bash
git clone https://github.com/mohammedfarves/recipe-finder-fastapi.git
cd recipe-finder-fastapi
```

---

### 🔹 Step 2: Create & Activate Virtual Environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac / Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 🔹 Step 3: Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary pydantic
```

---

### 🔹 Step 4: Configure Database

Set your PostgreSQL connection using an environment variable.

**Windows (PowerShell):**

```powershell
$env:DATABASE_URL="postgresql://postgres:12345678@localhost:5432/fastapi_todo"
```

**Mac / Linux:**

```bash
export DATABASE_URL="postgresql://postgres:12345678@localhost:5432/fastapi_todo"
```

---

### 🔹 Step 5: Insert Sample Recipe Data

```bash
python insert_recipes.py
```

Expected output:

```
Tables ensured.
Data inserted.
```

---

### 🔹 Step 6: Run the Application

```bash
python -m uvicorn project.main:app --reload
```

Server will start at:

```
http://127.0.0.1:8000
```

---

## 🚀 Usage

| Purpose          | URL                                        |
| ---------------- | -------------------------------------------|
| Swagger API Docs | [http://127.0.0.1:8000/docs]               |
| Frontend UI      | [http://127.0.0.1:8000/static/index.html]  |
| List Recipes API | [http://127.0.0.1:8000]                    |

---

## ☁ Deployment (Render)

* PostgreSQL hosted on Render
* Backend deployed as a Python Web Service
* Frontend served using FastAPI StaticFiles
* Environment variables used for secure DB access

---

## 📌 Tech Stack

* **Backend:** FastAPI, Python
* **Database:** PostgreSQL
* **ORM:** SQLAlchemy
* **Frontend:** HTML, CSS, JavaScript
* **Deployment:** Render

---

## 🏆 Why This Project Matters

* ✅ Real-world full-stack project
* ✅ Clean backend architecture
* ✅ Cloud deployment experience
* ✅ Beginner-friendly & production ready
* ✅ Perfect for resumes & portfolios

---

## 👨‍💻 Author

**Mohammed Farves**
📧 Email: [farveztech@gmail.com]
🔗 GitHub: [https://github.com/mohammedfarves]

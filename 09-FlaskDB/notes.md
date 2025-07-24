# 🚀 Day 9 – SQLAlchemy ORM in Flask (Structured Setup)  
  
## ✅ What I Learned Today  
  
- What is ORM (Object Relational Mapping)  
- How SQLAlchemy connects Flask with a real database  
- How to define database tables as Python classes (models)  
- How to create a proper folder structure for Flask with ORM  
- How to insert data into the database using route  
  
---  
  
## 🔍 What is ORM?  
  
ORM allows us to work with the database using **Python code** instead of raw SQL queries.  
  
**Example:**  
  
```python  
# Instead of raw SQL  
INSERT INTO users (name) VALUES ('Hardik')  
  
# ORM way in Python  
user = User(name="Hardik")  
db.session.add(user)  
db.session.commit()  
  
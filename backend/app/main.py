# app/main.py
from fastapi import FastAPI
from app.db.postgres import database

app = FastAPI(title="CypherChat Backend")

@app.on_event("startup")
async def connect_db():
    await database.connect()
    print("✅ Connected to Supabase PostgreSQL")

@app.on_event("shutdown")
async def disconnect_db():
    await database.disconnect()
    print("❌ Disconnected from Supabase PostgreSQL")

@app.get("/")
async def root():
    return {"message": "Supabase PostgreSQL connected successfully!"}

@app.post("/register")
async def register_user():
    # Placeholder for user registration logic
    return {"message": "User registration endpoint"}


@app.post("/login")
async def login_user():
    # Placeholder for user registration logic
    return {"message": "User login endpoint"}
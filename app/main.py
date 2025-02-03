from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
from .crud import create_user, get_user_by_email

app = FastAPI()

@app.post("/users/")
async def create_new_user(user: dict, db: AsyncSession = Depends(get_db)):
    existing_user = await get_user_by_email(db, user['email'])
    if existing_user:
        return {"error": "Email already registered"}
    return await create_user(db, user)

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI with PostgreSQL!"}

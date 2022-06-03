from typing import List
from uuid import UUID, uuid4
from fastapi import FastAPI
from models import User, Gender, Role

app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        firstName="Pius",
        lastName="Prince",
        email="piusprince@gmail.com",
        gender=Gender.male,
        roles=[Role.student]
    ),  
    User(
        id=uuid4(), 
        firstName="Dwight",
        lastName="Clayman",
        email="dwightclayman@gmail.com",
        gender=Gender.male,
        roles=[Role.admin, Role.user]
    )
]

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def register_user(user: User):
    db.append(user)
    return {"id": user}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return {"message": "User deleted"}

from fastapi import FastAPI
from app.routes import users

app = FastAPI()

app.include_router(users.user_route)
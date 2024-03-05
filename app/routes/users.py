from fastapi import APIRouter, Form
from app.repositories.user_repositorie import UserRepositorie
from app.schemas.users_schema import UserCreate, UserResponse, UserWithToken
from app.utils.authentication import authenticate_user

user_route = APIRouter(prefix="/user", tags=["USERS"])

@user_route.post("/register", response_model=UserResponse)
async def create_user(user_data: UserCreate):
    
    response = UserRepositorie.createUser(user_data.model_dump())
    
    return response

@user_route.get("/profile/{username}", response_model= list[UserResponse])
async def getUserbyid(username: str):
    
    response = UserRepositorie.getUsersbyUsername(username)
    
    return response

@user_route.post("/login", response_model=UserWithToken)
async def login(email_form = Form(...), password_form = Form(...)):
    
    user = authenticate_user(email_form, password_form)
    return user
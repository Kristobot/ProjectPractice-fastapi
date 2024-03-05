from pydantic import BaseModel, EmailStr
from typing import Optional, Annotated

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    
class UserWithToken(UserResponse):
    access_token: str
    type: Optional[str] = "Bearer"
    
class UserInDB(UserResponse):
    password: str
from app.services.security import verifyPassword
from app.models.users_table import UserTable
from app.repositories.user_repositorie import UserRepositorie
from fastapi import HTTPException, status

def authenticate_user(into_email, into_password):
    
    user: UserTable = UserRepositorie.getUserByEmail(into_email=into_email)
    
    if not verifyPassword(into_password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña es incorrecta")
    
    return user
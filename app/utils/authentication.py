from app.utils.security import verifyPassword
from app.repositories.user_repositorie import UserRepositorie
from fastapi import HTTPException, status
from app.utils.auth import generate_token
from app.schemas.users_schema import UserWithToken

def authenticate_user(into_email, into_password):
    
    user = UserRepositorie.getUserByEmail(into_email=into_email)
    
    if not verifyPassword(into_password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña es incorrecta")

    
    token = generate_token(user.email)
    
    return UserWithToken(id=user.id,username=user.username,email=user.email,access_token=token)
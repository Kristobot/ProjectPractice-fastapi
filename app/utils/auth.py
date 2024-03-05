from jose import jwt, JWTError
from app.schemas.users_schema import UserInDB
from datetime import datetime, timedelta

SECRET = "Gzg8OPXb6R1bSdLpCDkDT4I4qy1P2Ac6cl3Z9swp6LU="

def generate_token(user_email):
    
    payload = {
        "sub": user_email,
        "exp": datetime.utcnow() + timedelta(seconds=1200)
    }
    
    return jwt.encode(payload,SECRET)
    
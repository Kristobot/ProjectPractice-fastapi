from passlib.hash import bcrypt_sha256

def hashPassword(into_password: str) -> str:
    
    return bcrypt_sha256.hash(into_password)

def verifyPassword(plain_password: str, hashpwd: str) -> bool:
    
    if bcrypt_sha256.verify(plain_password, hashpwd):
        return True
    
    return False
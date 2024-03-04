from database.db import Database
from app.models.users_table import UserTable
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from pydantic import ValidationError
from fastapi import HTTPException, status
from app.services.security import hashPassword

class UserRepositorie:
    def __init__(self):
        self.session = Database.getSession()
        
    @property
    def getSession(self) -> Session:
        return self.session
    
    @staticmethod
    def createUser(user_data: dict):
        
        session = UserRepositorie().getSession
        
        try:
            
            user_data["password"] = hashPassword(user_data["password"])
            new_user = UserTable(**user_data)
            session.add(new_user)
            session.commit()
            session.refresh(new_user)
            
            return new_user
        
        except ValueError as v:
            session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User data Invalid: {v}")
        
        except IntegrityError as i:
            session.rollback()
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Datos Duplicados: {i}")
        
        finally:
            session.close()
        
    @staticmethod
    def getUsersbyUsername(into_username: str) -> list:
        
        session = UserRepositorie().getSession
        
        try:
            
            user = session.query(UserTable).filter(UserTable.username.like(f"%{into_username}%")).all()
            
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El ID no existe")
            
            return user
        
        except ValueError as v:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Debe ser un valor entero")
        
        finally:
            session.close()
            
    @staticmethod
    def getUserByEmail(into_email: str):
        
        session = UserRepositorie().getSession
        
        try:
            
            user = session.query(UserTable).filter_by(email = into_email).first()
            
            if not user:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="El Email ingresado no se encuentra registrado o es incorrecto")
            
            return user
        
        finally:
            session.close()
        
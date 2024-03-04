from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pymysql

class Database:
    
    def __init__(self):
        self.engine = create_engine("mysql+pymysql://root:123456@localhost/gestion_users")
        
    @property
    def getEngine(self):
        return self.engine
    
    @staticmethod
    def getSession():
        
        db = sessionmaker(bind=Database().getEngine)
        session = db()
        
        try:
            return session
        finally:
            session.close()
            



            
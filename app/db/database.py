from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .base import Base

#import db url from settings
from core.config import settings

from models.expense import Expense
from models.user import User

#create the db engine
engine = create_engine(settings.DATABASE_URL)

#create a configured session class
sessionLocal = sessionmaker(autocommit=False,autoflush=False, bind=engine)

#Dependency to get a db session
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
        
#Function to create all tables
def create_tables():
    Base.metadata.create_all(bind=engine)
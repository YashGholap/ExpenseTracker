# Application settings and Environment Variables
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

#load Environment Variables from .env files
load_dotenv()

class Settings(BaseSettings):
    #Application settings 
    PROJECT_NAME: str = "ExpenseTracker"
    DEBUG: bool = True
    
    #DB settings
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    
    #Security settings
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    
    class Config:
        #Allow environment variables to override the default values
        case_sensitive = True
        

#create an instance of the Settings class
settings = Settings()
    

from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

#class for User Base
class UserBase(BaseModel):
    username: str
    email: str
    
#schema for creating a user (user register)
class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=64)
    
    
#schema for returning a user data
class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
        
#schema for user Login
class UserLogin(BaseModel):
    email: EmailStr
    password: str 
    # = Field(..., min_length=6, max_length=64)
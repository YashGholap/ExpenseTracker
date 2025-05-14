from pydantic import BaseModel
from datetime import datetime


#Base Schema for common fields
class ExpenseBase(BaseModel):
    name: str
    amount: float
    category: str
    

#schema for creating an expense
class ExpenseCreate(ExpenseBase):
    pass


#schema for returning an expense(includes id and created_at)
class ExpenseResponse(ExpenseBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes: True #Enables orm Mode
        
        
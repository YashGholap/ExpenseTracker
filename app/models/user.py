from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship
from db.base import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True, nullable=False)
    email = Column(String,unique=True, index=True, nullable=False)
    password = Column(String,nullable=True)
    created_at = Column(DateTime,default=func.now())
    
    #relationship to Expense
    expenses = relationship("Expense", back_populates="user")
    
    
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})"
    


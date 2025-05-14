from sqlalchemy import Column, Integer, String, Float, DateTime, func, ForeignKey
from sqlalchemy.orm import relationship
from db.base import Base

class Expense(Base):
    __tablename__ = "expenses"
     
    #columns
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    amount = Column(Float, nullable=False)
    category = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now())
    
    #foreign key
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    #Relationship to User
    user = relationship("User", back_populates="expenses")
    
    def __repr__(self):
        return f"<Expense(id={self.id}, name={self.name}, amount={self.amount}, category={self.category})>"



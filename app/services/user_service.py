from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models.user import User
from core.security import hash_password
from sqlalchemy.exc import IntegrityError
from schemas.user import (
    UserCreate,
    UserLogin,
    UserResponse
)

def create_user(db: Session, user_data: UserCreate) -> UserResponse | None:
    try:
        hashed_pwd = hash_password(user_data.password)
        db_user = User(
            username = user_data.username,
            email = user_data.email,
            password = hashed_pwd
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        
        return UserResponse(
            id = db_user.id,
            username = db_user.username,
            email = db_user.email,
            created_at= db_user.created_at,
        )
    except IntegrityError:
        db.rollback()       
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username or email already exists"
        )

def get_user(db:Session, user_id: int) -> UserResponse:
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found."
            )
        
    return UserResponse(
            id = db_user.id,
            username = db_user.username,
            email = db_user.email,
            created_at= db_user.created_at,
        )
    
def login_user(db:Session, user_data: UserLogin):
    pass
from sqlalchemy.orm import Session
from sqlalchemy.exc import  SQLAlchemyError
from fastapi import HTTPException, status
from models.expense import Expense
from schemas.expense import ExpenseCreate, ExpenseResponse

def is_user(db: Session, user_id: int):
    user = db.query(Expense).filter(Expense.user_id == user_id).first()
    return user

#create a new Expense
def create_expense(db:Session, expense_data:ExpenseCreate, user_id: int) -> ExpenseResponse:
    try:
        db_expense = Expense(**expense_data.model_dump(), user_id = user_id)
        db.add(db_expense)
        db.commit()
        db.refresh(db_expense)
        return ExpenseResponse(
            id =  db_expense.id,
            name = db_expense.name,
            amount = db_expense.amount,
            category= db_expense.category,
            created_at= db_expense.created_at
        )
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
                            detail = f"Error creating expense: {str(e)}")

#Retrive all the expenses
def get_expenses(db:Session, user_id: int) -> list[ExpenseResponse]:
    user = is_user(db, user_id)
    if user:
        expenses = db.query(Expense).all()
        return [ExpenseResponse(
        id=expense.id,
        name=expense.name,
        amount=expense.amount,
        category=expense.category,
        created_at=expense.created_at
        ) for expense in expenses]
    else:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,
                            detail="Required Authorized access.")
#Fetch a specific expense by ID
def get_expense_by_id(db:Session, expense_id: int, user_id: int) -> ExpenseResponse | None:
    user = is_user(db,user_id)
    if user:
        db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
        if db_expense is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Expense with ID {expense_id} not found."
            )
        return ExpenseResponse(
            id=db_expense.id,
            name=db_expense.name,
            amount=db_expense.amount,
            category=db_expense.category,
            created_at=db_expense.created_at
        )

#update an existing Expense
def update_expense(db:Session, expense_id: int, update_data: ExpenseCreate, user_id: int) -> ExpenseResponse | None:
    try:
        if is_user(db, user_id):
            db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
            if db_expense is None:
                return None
            for key, value in update_data.model_dump().items():
                setattr(db_expense,key, value)
            db.commit()
            db.refresh(db_expense)
            return ExpenseResponse(
                id =  db_expense.id,
                name = db_expense.name,
                amount = db_expense.amount,
                category= db_expense.category,
                created_at= db_expense.created_at,
            )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error Updating expense: {str(e)}"
        )


#Delete an Expense
def delete_expense(db:Session, expense_id: int, user_id: int) -> ExpenseResponse | None:
    try:
        user = is_user(db,user_id)
        if user:
            db_expense = db.query(Expense).filter(Expense.id == expense_id).first()
            if db_expense is None:
                return None

            db.delete(db_expense)
            db.commit()

            return ExpenseResponse(
                id=db_expense.id,
                name=db_expense.name,
                amount=db_expense.amount,
                category=db_expense.category,
                created_at=db_expense.created_at
            )
    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error Deleting expense: {expense_id}"
        )
    
    
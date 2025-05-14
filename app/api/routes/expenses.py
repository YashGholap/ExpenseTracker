from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db
from models.user import User
from api.routes.user import get_current_user
from schemas.expense import ExpenseCreate, ExpenseResponse
from services.expense_service import (
    create_expense,
    get_expenses,
    get_expense_by_id,
    update_expense,
    delete_expense,
)

router = APIRouter()

#create a new expense
@router.post('/', response_model=ExpenseResponse)
def create_expense_route(expense: ExpenseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # print(f"Current User Id: {current_user.id}")
    return create_expense(db, expense, user_id = current_user.id)

#get all expensescd 
@router.get('/', response_model=list[ExpenseResponse])
def get_expenses_route(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_expenses(db, user_id = current_user.id)

#Get a specific expense by ID
@router.get('/{expense_id}', response_model=ExpenseResponse)
def get_expense__by_id_route(expense_id: int, db:Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    expense = get_expense_by_id(db, expense_id, user_id = current_user.id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found!")
    return expense

#Update an Existing Expense by ID
@router.put('/{expense_id}', response_model=ExpenseResponse)
def update_expense_by_id_route(expense_id: int, update_data: ExpenseCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    expense = update_expense(db, expense_id, update_data, user_id= current_user.id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found!")
    return expense

#Delete an Expense by ID
@router.delete('/{expense_id}',response_model=ExpenseResponse)
def delete_expense_by_id_route(expense_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    expense = delete_expense(db, expense_id, user_id = current_user.id)
    if expense is None:
        raise HTTPException(status_code=404, detail="Expense not found!")
    return expense
    


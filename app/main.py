from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from app.api.routes import users, expenses, auth
from api.routes.expenses import router as expense_router
from api.routes.user import  router as user_router
from db.database import create_tables
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating tables...")  # Debugging message
    create_tables()  # Explicitly create tables on startup
    yield 
    print("Shutting Server Down....")
    
#Initialize the FastAPI app
app = FastAPI(
    title="Expense Tracker App",
    description="A simple API to track expenses and manage users.",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Only allow frontend URL
    allow_credentials=True,
    allow_methods=["POST", "GET", "PUT", "DELETE"],  # Allowed HTTP methods
    allow_headers=["*"],  # Allow all header
)

app.include_router(expense_router, prefix="/expenses", tags=["expenses"])
app.include_router(user_router)

#include API Routes
# app.include_router(users.router, prefix="/users", tags=["users"])
# app.include_router(expenses.router, prefix="/expenses", tags = ["expenses"])
# app.include_router(auth.router, prefix="/auth", tags = ["auth"])


#Root endpoint
@app.get('/')
def read_root():
    return {"message": "Welcome to the Expense Tracker API!"}
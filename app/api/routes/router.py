from fastapi import APIRouter
from . import users, signup

base_router = APIRouter()

base_router.include_router(users.router, tags=["users"])
base_router.include_router(signup.router)
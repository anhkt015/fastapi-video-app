from fastapi import APIRouter
from auth.jwt_handler import create_token

router = APIRouter()

@router.post("/login")
def login(username: str):
    token = create_token(username)
    return {"access_token": token, "token_type": "bearer"}

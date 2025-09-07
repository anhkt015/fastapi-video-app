from fastapi import APIRouter, Form
from auth.jwt_handler import create_token

router = APIRouter()

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    # Giả sử bạn dùng tài khoản cứng để test
    if username == "admin" and password == "123":
        token = create_token(username)
        return {"access_token": token, "token_type": "bearer"}
    return {"error": "Sai thông tin đăng nhập"}

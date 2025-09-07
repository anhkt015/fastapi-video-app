# auth/jwt_handler.py
from jose import jwt, JWTError
from fastapi import HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from datetime import datetime, timedelta
import os

SECRET = os.getenv("JWT_SECRET", "your-secret")
ALGORITHM = "HS256"
bearer = HTTPBearer()

def create_token(username: str, expire_minutes: int = 60):
    payload = {
        "sub": username,
        "exp": datetime.utcnow() + timedelta(minutes=expire_minutes)
    }
    return jwt.encode(payload, SECRET, algorithm=ALGORITHM)

def verify_token(credentials: HTTPAuthorizationCredentials = bearer):
    try:
        jwt.decode(credentials.credentials, SECRET, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token không hợp lệ hoặc đã hết hạn"
        )

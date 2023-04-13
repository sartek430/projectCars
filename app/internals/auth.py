# Libs Imports
from fastapi import Depends, FastAPI, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import hashlib
# Local Imports
from routers.user import users

router = APIRouter()


def hash_password(password: str):
    return hashlib.sha256(f'{password}'.encode('utf-8')).hexdigest()


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    hashed_password = hash_password(form_data.password)
    for user in users:
        if user["name"] == form_data.username and hashed_password == user["password_hash"]:
            return {"access_token": user["name"], "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="Incorrect username or password")

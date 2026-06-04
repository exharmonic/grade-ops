
from fastapi import APIRouter, Depends
from app.oauth2 import get_current_user


router = APIRouter(
    prefix="/users",
    tags=["User"]
)

@router.get("/me")
async def read_users_me(current_user: dict = Depends(get_current_user)):
    return {
        "email": current_user.email,
        "role": current_user.role
    }
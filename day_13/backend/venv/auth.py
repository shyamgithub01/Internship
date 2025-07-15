# auth.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from models import Role

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Dummy function to get user role based on token
def get_current_user_role(token: str = Depends(oauth2_scheme)) -> Role:
    if token == "admin-token":
        return Role.ADMIN
    elif token == "editor-token":
        return Role.EDITOR
    elif token == "user-token":
        return Role.USER
    else:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

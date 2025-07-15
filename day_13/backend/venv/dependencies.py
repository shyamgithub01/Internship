# dependencies.py

from fastapi import Depends, HTTPException, status
from auth import get_current_user_role
from models import Role

def role_checker(allowed_roles: list[Role]):
    def checker(user_role: Role = Depends(get_current_user_role)):
        if user_role not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You don't have access to this resource",
            )
        return user_role
    return checker

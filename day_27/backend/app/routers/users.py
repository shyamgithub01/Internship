# # routers/users.py
# from fastapi import APIRouter, Depends, HTTPException, status, Query
# from sqlalchemy.orm import Session
# from db.session import SessionLocal
# from services import user_service
# from schemas import user
# from typing import Optional

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# users_router = APIRouter(prefix="/users", tags=["Users"])

# @users_router.post("/", response_model=user.UserOut, status_code=status.HTTP_201_CREATED)
# def create_user_endpoint(user_in: user.UserCreate, db: Session = Depends(get_db)):
#     return user_service.create_user(db, user_in)

# @users_router.get("/", response_model=list[user.UserOut])
# def get_all_users(db: Session = Depends(get_db)):
#     return user_service.get_all_users(db)

# @users_router.put("/me", response_model=user.UserOut)
# def update_current_user(
#     update_data: user.UserUpdate,
#     db: Session = Depends(get_db),
#     user_id: int = Query(..., description="Your user ID"),
# ):
#     updated = user_service.update_user(db, user_id, update_data)
#     if not updated:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     return updated

# @users_router.post("/upload-kyc", response_model=user.UserOut)
# def upload_kyc_endpoint(
#     kyc: user.KYCUpload,
#     db: Session = Depends(get_db),
#     user_id: int = Query(..., description="User ID uploading KYC"),
# ):
#     return user_service.upload_kyc(db, user_id, kyc)

# @users_router.get("/kyc-status", response_model=user.KYCStatus)
# def get_kyc_status(
#     db: Session = Depends(get_db),
#     user_id: Optional[int]   = Query(None, description="User ID"),
#     email:   Optional[str]   = Query(None, description="User Email"),
#     name:    Optional[str]   = Query(None, description="User Name"),
# ):
#     if not any([user_id, email, name]):
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Provide user_id, email, or name"
#         )
#     if user_id:
#         u = user_service.get_user_by_id(db, user_id)
#     elif email:
#         u = user_service.get_user_by_email(db, email)
#     else:
#         u = user_service.get_user_by_name(db, name)
#     if not u:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     return {"is_kyc_verified": u.is_kyc_verified}

# @users_router.get("/{user_id}", response_model=user.UserOut)
# def get_user_by_id_endpoint(user_id: int, db: Session = Depends(get_db)):
#     u = user_service.get_user_by_id(db, user_id)
#     if not u:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     return u

# @users_router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
# def delete_user(user_id: int, db: Session = Depends(get_db)):
#     deleted = user_service.delete_user(db, user_id)
#     if not deleted:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
#     return

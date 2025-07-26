# # services/user_service.py
# from sqlalchemy.orm import Session
# from models.user import User
# from schemas.user import UserCreate, UserUpdate, KYCUpload
# from utils.auth import hash_password
# from fastapi import HTTPException, status

# def get_all_users(db: Session):
#     return db.query(User).all()

# def get_user_by_id(db: Session, user_id: int):
#     return db.query(User).filter(User.id == user_id).first()

# def get_user_by_email(db: Session, email: str):
#     return db.query(User).filter(User.email == email).first()

# def get_user_by_name(db: Session, name: str):
#     return db.query(User).filter(User.name == name).first()

# def create_user(db: Session, user: UserCreate):
#     if get_user_by_email(db, user.email):
#         raise HTTPException(
#             status_code=status.HTTP_400_BAD_REQUEST,
#             detail="Email already registered"
#         )
#     hashed_pw = hash_password(user.password)
#     db_user = User(name=user.name, email=user.email, hashed_password=hashed_pw)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

# def update_user(db: Session, user_id: int, user_data: UserUpdate):
#     user_obj = get_user_by_id(db, user_id)
#     if not user_obj:
#         return None
#     for attr, value in user_data.dict(exclude_unset=True).items():
#         setattr(user_obj, attr, value)
#     db.commit()
#     db.refresh(user_obj)
#     return user_obj

# def delete_user(db: Session, user_id: int):
#     user_obj = get_user_by_id(db, user_id)
#     if not user_obj:
#         return None
#     db.delete(user_obj)
#     db.commit()
#     return True

# def upload_kyc(db: Session, user_id: int, kyc: KYCUpload):
#     user_obj = get_user_by_id(db, user_id)
#     if not user_obj:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             detail="User not found"
#         )
#     user_obj.kyc_document = kyc.document_url
#     user_obj.is_kyc_verified = False
#     db.commit()
#     db.refresh(user_obj)
#     return user_obj

# # schemas/user.py
# from pydantic import BaseModel, EmailStr, Field
# from typing import Optional
# from datetime import datetime

# class UserBase(BaseModel):
#     name: str
#     email: EmailStr

# class UserCreate(UserBase):
#     password: str

# class UserOut(UserBase):
#     user_id: int = Field(..., alias="id", description="Unique user identifier")
#     is_kyc_verified: bool
#     created_at: datetime

#     model_config = {
#         "from_attributes": True,
#         "populate_by_name": True,
#     }

# class UserUpdate(BaseModel):
#     name: Optional[str]
#     email: Optional[EmailStr]

# class KYCUpload(BaseModel):
#     document_url: str

# class KYCStatus(BaseModel):
#     is_kyc_verified: bool

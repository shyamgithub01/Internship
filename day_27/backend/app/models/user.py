# # models/user.py
# from sqlalchemy import Column, Integer, String, Boolean, DateTime
# from db.session import Base
# from datetime import datetime ,timezone
# from sqlalchemy.orm import relationship

# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, nullable=False)
#     email = Column(String, unique=True, nullable=False, index=True)
#     hashed_password = Column(String, nullable=False)
#     kyc_document = Column(String, nullable=True)
#     is_kyc_verified = Column(Boolean, default=False)
#     created_at = Column(DateTime, default=datetime.now(timezone.utc))

#     accounts = relationship("Account", back_populates="user")


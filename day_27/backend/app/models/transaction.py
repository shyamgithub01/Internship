# from sqlalchemy import Column, Integer, Float, String, ForeignKey, DateTime, Enum as SqlEnum
# from sqlalchemy.orm import relationship
# from db.session import Base
# from datetime import datetime
# import enum

# class TransactionType(str, enum.Enum):
#     deposit = "deposit"
#     withdraw = "withdraw"
#     transfer = "transfer"
#     imps = "imps"
#     neft = "neft"
#     reversal = "reversal"

# class Transaction(Base):
#     __tablename__ = "transactions"

#     id = Column(Integer, primary_key=True, index=True)
#     sender_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=True)
#     receiver_account_id = Column(Integer, ForeignKey("accounts.id"), nullable=True)
#     amount = Column(Float, nullable=False)
#     txn_type = Column(SqlEnum(TransactionType, name="transaction_type_enum"), nullable=False)
#     status = Column(String, default="completed")
#     initiated_by_user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
#     created_at = Column(DateTime, default=datetime.utcnow)
#     remarks = Column(String, nullable=True)

#     sender_account = relationship("Account", foreign_keys=[sender_account_id])
#     receiver_account = relationship("Account", foreign_keys=[receiver_account_id])

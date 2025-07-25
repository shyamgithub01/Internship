# services/auth.py
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from passlib.exc import UnknownHashError

from models.account import Account
from utils.security import hash_password, verify_password

def authenticate_account(db: Session, aadhar: str, password: str) -> Account:
    acct = db.query(Account).filter_by(aadhar_card_number=aadhar).first()
    if not acct:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")

    try:
        valid = verify_password(password, acct.password)
    except UnknownHashError:
        # legacy plaintext fallback
        if acct.password == password:
            valid = True
            # upgrade to bcrypt
            acct.password = hash_password(password)
            db.commit()
            db.refresh(acct)
        else:
            valid = False

    if not valid:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, "Invalid credentials")

    return acct

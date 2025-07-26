import secrets
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.account import Account
from utils.exceptions import raise_400, raise_404
from schemas.account import AccountCreate

def generate_account_number(db: Session) -> str:
    """Generate a unique 12-digit account number."""
    while True:
        num = "".join(secrets.choice("0123456789") for _ in range(12))
        if not db.query(Account).filter_by(account_number=num).first():
            return num

def get_all_accounts(db: Session):
    return db.query(Account).all()

def get_account_by_id(db: Session, account_id: int):
    acct = db.query(Account).filter_by(id=account_id).first()
    if not acct:
        raise_404(f"Account {account_id} not found")
    return acct

def create_account(db: Session, data: AccountCreate):
    print("📥 Incoming registration data:", data.dict())

    # Unique-field validations
    existing_email = db.query(Account).filter_by(email=data.email).first()
    existing_aadhar = db.query(Account).filter_by(aadhar_card_number=data.aadhar_card_number).first()
    existing_mobile = db.query(Account).filter_by(mobile_number=data.mobile_number).first()

    if existing_email:
        print("❌ Email already exists:", data.email)
        raise_400(f"Email {data.email} already in use")

    if existing_aadhar:
        print("❌ Aadhar already registered:", data.aadhar_card_number)
        raise_400("Aadhar already registered")

    if existing_mobile:
        print("❌ Mobile already registered:", data.mobile_number)
        raise_400("Mobile number already registered")

    # Create the account
    acct_num = generate_account_number(db)
    acct = Account(
        full_name=data.full_name,
        email=data.email,
        age=data.age,
        aadhar_card_number=data.aadhar_card_number,
        mobile_number=data.mobile_number,
        password=data.password,
        account_type=data.account_type,
        account_number=acct_num
    )
    db.add(acct)
    db.commit()
    db.refresh(acct)

    print("✅ Account created with number:", acct.account_number)
    return acct

def change_password(db: Session, aadhar: str, new_password: str):
    acct = db.query(Account).filter_by(aadhar_card_number=aadhar).first()
    if not acct:
        raise_404("Account not found")
    acct.password = new_password
    db.commit()
    db.refresh(acct)
    return acct

def delete_account(db: Session, aadhar: str):
    acct = db.query(Account).filter_by(aadhar_card_number=aadhar).first()
    if not acct:
        raise_404("Account not found")
    db.delete(acct)
    db.commit()

def authenticate_user(db: Session, email: str, password: str):
    user = db.query(Account).filter_by(email=email, password=password).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user

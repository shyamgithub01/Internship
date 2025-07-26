from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from routers.transactions import router as tx_router

from db.session import engine, Base
from fastapi import FastAPI
from routers.accounts import router as accounts_router


app = FastAPI()
app.include_router(accounts_router)



app = FastAPI(title="BankX API")

# 1) CORS setup – allow your Vite front‑end origin:
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.get('/')
def Welcome_To_Our_Bank():
    return {"message" : "welcome to our back"}
app.include_router(tx_router)

app.include_router(accounts_router)


Base.metadata.create_all(bind=engine)





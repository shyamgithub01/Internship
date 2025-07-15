# main.py
from fastapi import FastAPI , Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

app = FastAPI()

# Allow frontend access (e.g. from React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # React app origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI"}




# Custom middleware to log requests
class LogMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        print(f"Incoming request: {request.method} {request.url}")
        response = await call_next(request)
        print("Response sent")
        return response

app.add_middleware(LogMiddleware)

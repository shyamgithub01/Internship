from fastapi import FastAPI, Depends

app = FastAPI()


def get_current_user():
    return "Shyam"


@app.get("/profile/")
def show_profile(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello, {current_user}!"}

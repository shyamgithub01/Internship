# from fastapi import FastAPI, BackgroundTasks

# app = FastAPI()

# def write_log(message: str):
#     with open("log.txt", "a") as file:
#         file.write(message + "\n")

# @app.post("/send-message")
# def send_message(background_tasks: BackgroundTasks):
#     # User ko turant response milta hai
#     background_tasks.add_task(write_log, "Message sent at 5 PM")
#     return {"message": "Message sent, log likh diya jayega background mein"}

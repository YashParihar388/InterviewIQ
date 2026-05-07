from fastapi import FastAPI
from database import check_connection

app = FastAPI()

@app.get('/')
def home():
    return "api is running"


@app.on_event("startup")
def startup():
    print("hey")
    check_connection()

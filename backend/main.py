from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return "api is running"


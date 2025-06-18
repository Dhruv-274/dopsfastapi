import fastapi
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
async def base():
    return "message": "Hello, World!"
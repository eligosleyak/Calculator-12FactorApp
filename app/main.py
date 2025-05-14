from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to the CalculatorAPI"}


@app.get("/add/{a}/{b}")
async def add(a: int, b: int):
    return {"result": a + b}

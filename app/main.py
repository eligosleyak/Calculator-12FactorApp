from fastapi import FastAPI, HTTPException

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to the CalculatorAPI"}


@app.get("/add/{a}/{b}")
async def add(a: int, b: int):
    return {"result": a + b}


@app.get("/subtract/{a}/{b}")
async def subtract(a: int, b: int):
    return {"result": a - b}


@app.get("/multiply/{a}/{b}")
async def multiply(a: int, b: int):
    return {"result": a * b}


@app.get("/divide/{a}/{b}")
async def divide(a: int, b: int):
    return {"result": a / b}

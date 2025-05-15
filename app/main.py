"""
Calculator API - A simple FastAPI application that provides basic arithmetic operations
through RESTful endpoints.
"""

from fastapi import FastAPI, HTTPException

# Initialize FastAPI application
app = FastAPI(
    title="Calculator API",
    description="A simple API that performs basic arithmetic operations",
    version="1.0.0",
)


@app.get("/")
async def welcome():
    """
    Welcome endpoint that returns a greeting message.

    Returns:
        dict: A welcome message
    """
    return {"message": "Welcome to the CalculatorAPI"}


@app.get("/add/{a}/{b}")
async def add(a: int, b: int):
    """
    Add two numbers together.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        dict: Result of addition
    """
    return {"result": a + b}


@app.get("/subtract/{a}/{b}")
async def subtract(a: int, b: int):
    """
    Subtract second number from first number.

    Args:
        a (int): First number (minuend)
        b (int): Second number (subtrahend)

    Returns:
        dict: Result of subtraction
    """
    return {"result": a - b}


@app.get("/multiply/{a}/{b}")
async def multiply(a: int, b: int):
    """
    Multiply two numbers.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        dict: Result of multiplication
    """
    return {"result": a * b}


@app.get("/divide/{a}/{b}")
async def divide(a: int, b: int):
    """
    Divide first number by second number.

    Args:
        a (int): First number (dividend)
        b (int): Second number (divisor)

    Returns:
        dict: Result of division

    Raises:
        HTTPException: If attempting to divide by zero
    """
    if b == 0:
        raise HTTPException(status_code=400, detail="Cannot divide by zero")
    return {"result": a / b}

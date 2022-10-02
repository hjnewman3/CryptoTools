from fastapi import APIRouter
from src.models import SquareAndMultiply

router = APIRouter(
    prefix='/square-and-multiply',
    tags=['sqaure and multiply']
)

steps = []

@router.get("/")
def square_and_multiply(x: int, e: int, m: int):
    result = x
    binary_e = bin(e)[3:]
    for binary_digit in binary_e:
        if int(binary_digit) == 0:
            result = __square(binary_digit, result, m)
        else:
            result= __square(binary_digit, result, m)
            result = __multiply(binary_digit, result, x, m)
    return SquareAndMultiply.Result(base = x, exponent = e, mod = m, binary = binary_e, result = result, steps = steps).dict()
    
def __multiply(binaryDigit: int, result: int, x: int, m: int):
    multiply =  (result * x) % m
    operation = f"{result} * {x} % {m} = {multiply}"
    steps.append(SquareAndMultiply.Steps(binary_digit = binaryDigit, operation = operation))
    return multiply

def __square(binaryDigit: int, x: int, m: int):
    square = x**2 % m
    operation = f"{x} * {x} % {m} = {square}"
    steps.append(SquareAndMultiply.Steps(binary_digit = binaryDigit, operation = operation))
    return square
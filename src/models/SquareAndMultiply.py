from pydantic import BaseModel

class Result(BaseModel):
    base: int
    exponent: int
    mod: int
    binary: str
    result: int
    steps: list

class Steps(BaseModel):
    binary_digit: int
    operation: str
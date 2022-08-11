from pydantic import BaseModel

class Result(BaseModel):
    n: int
    phi_n: int
    e: int
    d: int
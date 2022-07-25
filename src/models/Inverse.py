from pydantic import BaseModel

class ExtendedEuclidean(BaseModel):
    gcd: int
    x: int
    y: int

class MultiplicativeInverse(BaseModel):
    inverse: int

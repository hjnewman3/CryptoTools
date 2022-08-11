from pydantic import BaseModel

class Inverse(BaseModel):
    inverse: int
    extended_euclidean: object
    
class Algorithm(BaseModel):
    gcd: int
    x: int
    y: int

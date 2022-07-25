from fastapi import APIRouter
from models import GreatestCommonDivisor

router = APIRouter(
  prefix='/gcd',
  tags=['gcd']
)

@router.get("/")
def gcd(x: int, n: int):
  result = __gcd(x, n)
  return GreatestCommonDivisor.GCD(gcd = result)

def __gcd(x: int, n: int):
  if x < n:
    x, n = n, x

  if n == 0:
    return x
  else:
    return __gcd(n, x % n)
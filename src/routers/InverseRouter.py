from fastapi import APIRouter
from models import Inverse
from routers import GreatestCommonDivisorRouter

router = APIRouter(
  prefix='/inverse',
  tags=['inverse']
)

@router.get("/")
def multiplicative_inverse(a: int, b: int):
  if GreatestCommonDivisorRouter.gcd(a, b).gcd != 1:
    return Inverse.MultiplicativeInverse(inverse = 0).dict()

  result = __extended_euclidean(a, b)
  return Inverse.MultiplicativeInverse(inverse = result[0]).dict()

@router.get("/euclidean")
def extended_euclidean(a, b):
  result = __extended_euclidean(a, b)
  return Inverse.ExtendedEuclidean(gcd = result[2], x = result[1], y = result[0]).dict()

def __extended_euclidean(a, b):
  a = int(a)
  b = int(b)
  
  if b == 0:
    return 1, 0, a

  else:
    q = a // b
    r = a % b
    x, y, gcd = __extended_euclidean(b, r)
    return y, x - q * y, gcd

from fastapi import APIRouter
from models import ExtendedEuclidean
from routers import GreatestCommonDivisorRouter

router = APIRouter(
  prefix='/inverse',
  tags=['inverse']
)

@router.get("/")
def inverse(a: int, b: int):
  # if GreatestCommonDivisorRouter.gcd(a, b).gcd != 1:
  #   return ExtendedEuclidean.Inverse(inverse = 0).dict()

  result = __extended_euclidean(a, b)
  extended_euclidean = ExtendedEuclidean.Algorithm(gcd = result[2], y = result[1], x = result[0])
  return ExtendedEuclidean.Inverse(inverse = result[0], extended_euclidean = extended_euclidean)

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

from fastapi import APIRouter

router = APIRouter(
  prefix='/gcd',
  tags=['gcd']
)

@router.get("/")
def gcd(x: int, n: int):
  gcd = __gcd(x, n)
  return { 'GCD': f'{gcd}' }

def __gcd(x: int, n: int):
  if x < n:
    x, n = n, x

  if n == 0:
    return x
  else:
    return __gcd(n, x % n)
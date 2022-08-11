from fastapi import APIRouter
from models import RSA
from routers import ExtendedEuclideanRouter, GreatestCommonDivisorRouter

router = APIRouter(
  prefix='/rsa',
  tags=['rsa']
)

@router.get("/")
def rsa(p: int, q: int, plain: int):
    if not __is_prime(p):
        return f"{p} is not a prime number"
    
    if not __is_prime(q):
        return f"{q} is not a prime number"

    n = p * q
    phi_n = (p-1) * (q-1)
    e = __find_e(phi_n)
    d = __find_d(e, phi_n)

    print(f"e: {e}")
    print(f"d: {d}")

    encrypted = (plain ** e) % n
    decrypted = (encrypted ** d) % n

    return {"e": e, "d": d, "n": n, "phi_n": phi_n, "public key": f"({n},{e})", "private key": f"({n},{d})", "encrypted": encrypted, "decrypted": decrypted}

def __find_d(a: int, b: int):
    return ExtendedEuclideanRouter.inverse(a, b).inverse

def __find_e(phi_n: int):
    possible_e = [65537, 257, 7, 5, 3]
    for number in possible_e:
        if (phi_n > number):
            if GreatestCommonDivisorRouter.gcd(number, phi_n).gcd == 1:
                return number

def __is_prime(possible_prime):
    if possible_prime == 1:
        return False
    elif possible_prime == 2:
        return True
    else:
        for number in range(2, possible_prime):
            if(possible_prime % number == 0):
                return False
        return True    

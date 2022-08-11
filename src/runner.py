import random
from cryptotools import CryptoTools
ct = CryptoTools()

# print(f"gcd of 24 18: {ct.gcd(24, 18)}")

# print(f"inverse: {ct.inverse(4864, 3458 )}")
# print(f"inverse: {ct.inverse(4864, 3458 , 'yes')}")

#print(f"sq mult: {ct.sq_mult(23, 373, 747)}")
#print(f"sq mult: {ct.sq_mult(3, 45, 7)}")

# runs a test on the RSA function
#print(ct.rsa(5, 11, 7, 5))
print(ct.rsa(3, 11, 7, 3))

# runs a test on the CRT function
# verify that x = 721
#print(ct.crt(31, 37, 17, 2))


def nBitRandom(n):
   
    # Returns a random number
    # between 2**(n-1)+1 and 2**n-1'''
    return(random.randrange(2**(n-1)+1, 2**n-1))

print(nBitRandom((2**4)+1))

print ((421*-29) + (111*110))

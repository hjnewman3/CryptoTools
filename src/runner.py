from cryptotools import CryptoTools
ct = CryptoTools()

# print(f"gcd of 24 18: {ct.gcd(24, 18)}")

# print(f"inverse: {ct.inverse(4864, 3458 )}")
# print(f"inverse: {ct.inverse(4864, 3458 , 'yes')}")

print(f"sq mult: {ct.sq_mult(14, 3, 26)}")

# runs a test on the RSA function
#print(ct.rsa(5, 11, 7, 5))

# runs a test on the CRT function
# verify that x = 721
#print(ct.crt(31, 37, 17, 2))
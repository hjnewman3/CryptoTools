from cryptotools import CryptoTools
ct = CryptoTools()

# runs a test on the RSA function
print(ct.rsa(5, 11, 7, 5))

# runs a test on the CRT function
# verify that x = 721
print(ct.crt(31, 37, 17, 2))
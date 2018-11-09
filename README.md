# CryptoTools
I'm studying Cryptography at the University of New Orleans, CSCI 4130. I developed a library to assist in the calculations used during the course. 

## Functions:
- gcd(x, n)
- inverse(x, n, showTable=None)
- sq_mult(x, e, m)
- rsa(p, q, e, x)
- crt(p, q, e, y)

### gcd():
Takes in two parameters and returns the gcd (greatest common divisor) or those numbers.

### inverse():
Takes in two parameters, with an optional third parameter. When the function is given only two parameters it will return the inverse of the two numbers. When the third parameter is passed in it will return the full extended euclidean algorithm.

### sq_mult():
Takes in three parameters: a base value as an x, an exponent value as e, and a modulus value as m. The function first cycles through the exponent one bit at a time, showing the steps toward the final result. Then a visual display of the square and mult operations as the binary exponent is iterated through.

### rsa():
Takes in four parameters and calculates the encrypt and decrypt values for RSA encryption.

### crt():
Takes in four parameters and calculates all of the different values for the CRT decryption.
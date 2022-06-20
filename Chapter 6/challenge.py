# Fermat primality test
import math, random

def get_coprime(n):
    while True:
        coprime = random.randrange(n)
        if math.gcd(coprime, n) == 1:
            return coprime
 
 
def fermat_primality(n, count = 1):
    for _ in range(count):
        a = get_coprime(n)
        if (a ** (n-1)) % n != 1:
            return False
    return True


for prime in [2, 3, 5, 7, 11, 13, 17, 19]:
    print(fermat_primality(prime))

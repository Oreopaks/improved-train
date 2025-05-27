import math
import random

def is_prime(n: int) -> bool:
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def gcd(a: int, b: int) -> int:
    return a if b == 0 else gcd(b, a % b)

def multiplicative_inverse(e: int, phi: int) -> int:
    def extended_gcd(a, b):
        if b == 0: return (a, 1, 0)
        g, x, y = extended_gcd(b, a % b)
        return (g, y, x - (a // b) * y)
    
    g, x, _ = extended_gcd(e, phi)
    if g != 1: raise ValueError("No inverse exists")
    return x % phi

def generate_keypair(p: int, q: int) -> tuple:
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime")
    if p == q: raise ValueError("p and q cannot be equal")
    
    n = p * q
    phi = (p-1) * (q-1)
    
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)
    
    d = multiplicative_inverse(e, phi)
    return ((e, n), (d, n))
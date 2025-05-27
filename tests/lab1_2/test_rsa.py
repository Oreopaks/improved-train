import pytest
from src.lab1_2.RSA import generate_keypair, is_prime, gcd, multiplicative_inverse

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(17) is True
    assert is_prime(15) is False
    assert is_prime(1) is False

def test_gcd():
    assert gcd(12, 15) == 3
    assert gcd(35, 49) == 7
    assert gcd(17, 22) == 1

def test_multiplicative_inverse():
    assert multiplicative_inverse(7, 40) == 23
    assert multiplicative_inverse(3, 20) == 7

def test_keypair_generation():
    pub, priv = generate_keypair(17, 19)
    assert isinstance(pub, tuple) and len(pub) == 2
    assert isinstance(priv, tuple) and len(priv) == 2
    assert pub[1] == priv[1]

def test_invalid_primes():
    with pytest.raises(ValueError):
        generate_keypair(4, 7)
    with pytest.raises(ValueError):
        generate_keypair(7, 7)
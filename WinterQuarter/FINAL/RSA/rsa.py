import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mInverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:


import random, math
lowerBound = input("\nEnter a lower bound (maybe 500 for faster) ")
largePrime = input("Enter an upper bound (maybe 1000 for faster) ")

def isPrime(num):
    if num == 2:
        return True
    for i in range(2, num - 1):
        if num % i == 0:
            return False
    return True

primes = [i for i in range(lowerBound,largePrime) if isPrime(i)]
p = random.choice(primes)
q = random.choice(primes)
n = p * q
z = (p - 1) * (q - 1)
e = random.choice(primes)
d = 0

while(e >= z):
    e = random.choice(primes)

for i in range (2, n):
    if ((e * i) % z == 1):
        d = i

m = 12
c = (m ** e) % n
message = (c ** d) % n

print("\n")
print("Original Message: ", m)
print("Encrypted Message: ", c)
print("Decrypted Message: ", message)
print("\n")

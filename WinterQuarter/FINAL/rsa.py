p = 5
q = 7
n = p * q
z = (p - 1) * (q - 1)
e = 31
d = 1

for i in range (2, n):
    if ((e * i) % z == 1):
        d = i

m = 12
c = (m ** e) % n
message = (c ** d) % n

print("Original Message: ", m)
print("Encrypted Message: ", c)
print("Decrypted Message: ", message)

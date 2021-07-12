import ChrEnD
from math import sqrt

encrypted = ChrEnD.encrypt('hello')
decrypted = ChrEnD.decrypt(encrypted)

print(encrypted)
print(decrypted)
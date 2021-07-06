import ChrEnD
from math import sqrt

encrypted = ChrEnD.encrypt('hello', modifier='(self * len(word)) ** 2')
decrypted = ChrEnD.decrypt(a, modifier='sqrt(self) / len(word)')

print(encrypted)
print(decrypted)
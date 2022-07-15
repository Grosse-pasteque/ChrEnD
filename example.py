import chrend


seed = chrend.seed(turns=1, modifiers=[("+", "%l"), ("*", 2)])
print(seed)


encrypted = chrend.encrypt('hello ma boi :)', seed=seed)
print(repr(encrypted))

tencrypted = chrend.transform(encrypted)
print(repr(tencrypted))

encrypted = chrend.untransform(tencrypted)
print(repr(encrypted))

decrypted = chrend.decrypt(encrypted, seed=seed)
print(repr(decrypted))


"""
If my math doesn't sucks:

should be better than SHA-256:

	2 ** 256  VS  10027035 ** 12

should be better than SHA-512:

	2 ** 256  VS  10027035 ** 23


"""
print('Beat SHA-256:', chrend.combinations(1, 12, 0x110000) > 2 ** 256)
print('Beat SHA-512:', chrend.combinations(1, 23, 0x110000) > 2 ** 512)

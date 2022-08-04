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

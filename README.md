# Chr - EnD [0.5.0]

## By Big watermelon#6705

-------------


### How it works ?

Python can transform letter to their index which is inside of the utf-8 table
```py
ord('a')     -> 97
chr(97)      -> 'a'
```

Simplified explainations:

1) text -> list
```py
text = list(text)

"hello" -> ['h', 'e', 'l', 'l', 'o']
```

2) each char -> ord(char)
```py
ord('h') -> 104
```

3) apply mathematical operations on the obtained number with modifiers
```py
104 -> 108 (+4)
```

4) return joined text
```py
'.'.join(text)

["108", "105", "112", "112", "116"] -> "108.105.112.112.116"
```

5) repeat 1, 2, 3 and 4 for number of required turns


-------------


### Functions:

You have at your disposition these function:
- **seed**
- **encrypt**
- **decrypt**
- **transform**
- **untransform**
- **combinations**

```py
import chrend

# all the allowed (operators, values): chrend.OPERATORS, chrend.CONV
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
```

##### Seeds

Seeds works like in minecraft:

But be careful, modifiers are math operations so one modifier can be equal to another.
Example bellow

```py
import chrend

seed_one = chrend.seed(turns=1, modifiers=[("<<", 4)])
# 0x1a4b5

seed_two = chrend.seed(turns=3, modifiers=[("*", 16)])
# 0x1a16b2

encrypted_one = chrend.encrypt('text', seed=seed_one)
encrypted_two = chrend.encrypt('text', seed=seed_two)

print(encrypted_one == encrypted_two)
# shows: True
```

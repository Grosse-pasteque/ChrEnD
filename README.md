# Chr - EnD [0.4.0]

## By Grosse pastèque#6705

-------------


### How it works ?

Python can transform letter to their index which is inside of the utf-8 table
```py
ord('a') 	-> 97
chr(97)		-> 'a'
```

Simplified explainations:

1) text -> list
```py
text = list(text)

'hello' -> ['h', 'e', 'l', 'l', 'o']
```

2) each char -> ord(char)
```py
ord('h') -> 104
```

3) return joined text
```py
'.'.join(text)

['104', '101', '108', '108', '111'] -> '104.101.108.108.111'
```

4) repeat 1, 2, 3 for number of required turns


-------------


### Usage:

You have at your disposition two function:
- **ChrEnD.encrypt()**
- **ChrEnD.decrypt()**

```py
import ChrEnD

encrypted = ChrEnD.encrypt('hello')
encrypted = ChrEnD.decrypt(encrypted)

print(encrypted)
print(decrypted)
```

##### Arguments

| argument  | type  | default (None = not default)  | explainations  |
| ------------ | ------------ | ------------ | ------------ |
| text  | *str* | None  | The text that you want to encrypt.  |
| turns  | *int*  | 1  | Text will be encrypted in loop in range(turns).  |
| modifier  | *str*  | 'self'  | If you want to execute modification on the `ord(char)`, `self` corespond to the number, `word` to the original word. his modifier will be passed into `eval()`.  |
| get_layers  | *bool*  | False  | Return the encrypted/decrypted text and all the layers of the text.  |
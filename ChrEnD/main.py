def StrtoList(s: str):
	l = []
	for char in s: l.append(char)
	return l

def ListtoStr(l: list):
	s = ''
	for char in l: s += char
	return s

def encrypt(text: str, turns=1):
	text = StrtoList(text.replace(' ', ';'))
	for i in range(turns):
		encrypted = ""
		for char in text:
			if char != ';': encrypted += f"{ord(char)}."
			else: encrypted += ';'
		encrypted = encrypted.replace(encrypted[:], encrypted[:-1]).replace('.;', ';')
		if turns > 0: text = StrtoList(encrypted)
	return encrypted

def decrypt(text: str, turns=1):
	text = text.replace(';', '. .').split('.')
	for i in range(turns):
		decryted = ""
		for char in text:
			if char not in [' ', '']: decryted += chr(int(char))
			else: decryted += ' '
		if turns > 0: text = decryted.replace(' ', ';').replace(';', '. .').split('.')
	return decryted
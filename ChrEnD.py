def encrypt(text: str, turns=1, modifier='self'):
	text = list(text)
	org_text = text

	for i in range(turns):
		
		encrypted = []
		for char in text:
			encrypted.append(str(eval(modifier\
				.replace('self', str(ord(char)))\
				.replace('word', repr(org_text))
			)))
		
		text = list('.'.join(encrypted))
	return '.'.join(encrypted)


def decrypt(text: str, turns=1, modifier='self'):
	text = text.split('.')
	org_text = text

	for i in range(turns):
		decrypted = ''
		for char in text:
			expression = modifier\
				.replace('self', char)\
				.replace('word', repr(org_text))

			decrypted += chr(int(eval(expression)))
		
		text = decrypted.split('.')
	return ''.join(decrypted)
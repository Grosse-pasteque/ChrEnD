def encrypt(text: str, turns=1, modifier='self', get_layers=False):
	layers = []

	org_text = text
	layers.append(text)

	text = list(text)
	layers.append(text)

	layers.append([])
	for i in range(turns):
		encrypted = []
		
		for char in text:
			encrypted.append(str(eval(modifier\
				.replace('self', str(ord(char)))\
				.replace('word', repr(org_text))
			)))
		
		layers[2].append('.'.join(encrypted))
		text = list('.'.join(encrypted))

	if get_layers:
		return '.'.join(encrypted), layers

	return '.'.join(encrypted)


def decrypt(text: str, turns=1, modifier='self', get_layers=False):
	layers = []

	org_text = text
	layers.append(text)

	text = text.split('.')
	layers.append(text)

	layers.append([])
	for i in range(turns):
		decrypted = ''

		for char in text:
			expression = modifier\
				.replace('self', char)\
				.replace('word', repr(org_text))

			decrypted += chr(int(eval(expression)))

		layers[2].append(decrypted)
		text = decrypted.split('.')

	if get_layers:
		return decrypted, layers

	return decrypted
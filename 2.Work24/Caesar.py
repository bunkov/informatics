class Caesar:
	alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

	def __init__(self, key):
		lowercase_code = {self.alphabet[i]:self.alphabet[(i+key)%len(self.alphabet)] for i in range(len(self.alphabet))}
		uppercase_code = {self.alphabet[i].upper():self.alphabet[(i+key)%len(self.alphabet)].upper() for i in range(len(self.alphabet))}
		self._encode = dict(lowercase_code)
		self._encode.update(uppercase_code)
		self._decode = invert_dict(self._encode)

	def encode(self, line):
		if len(line) == 1:
			return self._encode[line] if line in self._encode else line
		else:
			return ''.join([self.encode(char) for char in line])

	def decode(self, line):
		if len(line) == 1:
			return self._decode[line] if line in self._decode else line
		else:
			return ''.join([self.decode(char) for char in line])

def invert_dict(d):
    newdict = {}
    for (k, v) in d.items():
        newdict.setdefault(v, []).append(k)
        newdict[v] = ''.join(str(elem) for elem in newdict[v])
    return newdict

key = int(input('Введите ключ:'))
cipher = Caesar(key)
print('Кодирование')
line = input()
while line:
	print(cipher.encode(line))
	line = input()
print('Декодирование')
line = input()
while line:
	print(cipher.decode(line))
	line = input()

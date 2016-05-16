import os
class Monoalphabet:
	alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

	def __init__(self, keytable = alphabet):
		lowercase_code = {self.alphabet[i]:keytable[self.alphabet[i]] for i in range(len(self.alphabet))}
		uppercase_code = {self.alphabet[i].upper():keytable[self.alphabet[i]].upper() for i in range(len(self.alphabet))}
		self._encode = dict(lowercase_code)
		self._encode.update(uppercase_code)
		self._decode = invert_dict(self._encode)

	def encode(self, line): # Играет роль и кодировщика, и декодировщика
		if len(line) == 1:
			return self._encode[line] if line in self._encode else line
		else:
			return ''.join([self.encode(char) for char in line])
	def decode(self, line):
		if len(line) == 1:
			return self._decode[line] if line in self._decode else line
		else:
			return ''.join([self.decode(char) for char in line])

def decoder(line, sample = 'Chehov_palata.txt'): # Промежуточный этап декодирования
	alph = set(Monoalphabet.alphabet)
	keytable = {} # Таблица соответствий
	sample_chars_f = frequency_analysis(sample)
	line_chars_f = frequency_analysis(line)
	print([value for value in sample_chars_f], len([value for value in sample_chars_f]))
	print([value for value in line_chars_f], len([value for value in line_chars_f]))
	for line_char in line_chars_f:
		minim = line_chars_f[line_char]
		for sample_char in sample_chars_f:
			# Считаем, что частота образцового символа минимально отличается от частоты данного
			temp_min = abs(sample_chars_f[sample_char] - line_chars_f[line_char])
			# Если угадали
			if temp_min < minim:
				minim = temp_min
				right_char = sample_char # Найден потенциально верный символ
				if right_char in alph: # Попытка сделать лучше: не сопоставлять одному символу несколько
					alph.remove(right_char)
				else:
					right_char = '`'
		keytable.setdefault(right_char, line_char) # Добавить пару заменяющий символ/истинный символ
	for char in Monoalphabet.alphabet:
		if char not in keytable:
			keytable.setdefault(char, char)
	return keytable

def frequency_analysis(file_name):
	chars_f = {} # Создать список частот
	n = 0 # Счетчик кол-ва всех символов
	
	if os.path.isfile(file_name): # Если на входе файл (для заполнения списка частот)
		data_file = open(file_name)
		iterator = data_file.read() # Итерируемый объект - весь текст
		data_file.close()
	else:
		iterator = file_name # Если на входе строка (для декодирования)
	
	for char in iterator:
		low_char = char.lower() # Перевести все символы в нижний регистр
		if low_char in Monoalphabet.alphabet:
			if low_char in chars_f: # Символ уже занесен в список частот
				chars_f[low_char] += 1
			else:
				chars_f.setdefault(low_char, 1)
			n += 1
	for char in chars_f:
		chars_f[char] /= n
	return chars_f

def invert_dict(d):
	newdict = {}
	for (k, v) in d.items():
		newdict.setdefault(v, k)
	return newdict

line = input()
cipher = Monoalphabet(decoder(line))
print(cipher.encode(line))
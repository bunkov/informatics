inp = open('license.txt')
c = inp.read(1)
s = c
Words = dict()

while len(c) > 0:
	if s[-1] == ' ' or s[-1] == '\n': # Если слово закончилось
		# s[:-1] - слово без символа, который сообщил, что слово закончилось
		if s[:-1].lower() in Words: # Слово уже встречалось
			Words[s[:-1].lower()] += 1
		else:
			Words[s[:-1].lower()] = 1
		while len(c) > 0 and (s[-1] == ' ' or s[-1] == '\n'):
			c = inp.read(1) # Идем до следующего слова
			s = c
	else:
		c = inp.read(1)
		s += c

if s in Words: # Последнее слово
	Words[s] += 1
else:
	Words[s] = 1

max = 0
for key in Words:
	if max < Words[key]:
		max = Words[key]
		key_max = key
print(key_max, Words[key_max])
inp.close()
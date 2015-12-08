enru = open('en-ru.txt')
inp = open('input.txt')
out = open('output.txt','w')
s = enru.readline().rstrip()
EnRu = dict()

while len(s) > 0:
	en, ru = s.split('\t-\t')
	EnRu[en] = ru
	s = enru.readline().rstrip()

s = inp.readline().rstrip()
while len(s) > 0:
	en = list(s.split())
	ru = ' '
	for i in en:
		if i.lower().replace('.','') in EnRu:
			ru += EnRu[i.lower().replace('.','')] + ' '
		else:
			ru += i + ' '
	print(ru, file = out)
	s = inp.readline().rstrip()

inp.close()
enru.close()
out.close()

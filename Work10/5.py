enru = open('en-ru.txt')
inp = open('input.txt')
out = open('ru-en.txt','w')
s = enru.readline().rstrip()
EnRu = dict()

while len(s) > 0:
	en, ru = s.split('\t-\t')
	EnRu[en] = ru
	s = enru.readline().rstrip()

lst = list(EnRu.values())
lst.sort()

RuEn = dict()
RuEn = {EnRu[en] :en for en in EnRu}
for i in lst:
	print(i,'\t-\t',RuEn[i],sep='',file=out)
inp.close()
enru.close()
out.close()

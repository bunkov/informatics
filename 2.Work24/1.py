def invert_dict(d):
	newdict = {}
	for (k, v) in d.items():
		newdict.setdefault(v, []).append(k)
		newdict[v] = ''.join(str(elem) for elem in newdict[v])
	return newdict
d = {1:'one', 2:'two', 3:'three'}
print(invert_dict(d))

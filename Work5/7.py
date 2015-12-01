inp = open('int_data.txt', 'r')

int_arr = list(map(int, inp.readlines()))

max_f = min_f = None
freq = [0]*101
for i in range(101): # 0-100
	freq[i] = int_arr.count(i)
	if max_f is None or max_f < freq[i]:
		max_f = freq[i]
		max_f_elem = i
	if min_f is None or min_f > freq[i]:
		min_f = freq[i]
		min_f_elem = i
	#print(i, 'was', freq[i], ' times')
print(max_f_elem, 'was', max_f, 'times')
print(min_f_elem, 'was', min_f, 'times')

kolvo = 0
for i in range(101):
	if freq[i] != 0:
		kolvo += 1
print(kolvo, 'different numbers')

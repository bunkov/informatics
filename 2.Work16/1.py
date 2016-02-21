import sys
n = 0
for arg in sys.argv[1:]:
	if len(arg)%3 == 0:
		n += 1
print(n)
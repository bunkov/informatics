import sys
import os
for name in sys.argv[1:]:
	if os.path.isfile(name):
		f = open(name, 'r')
		strings=[s.rstrip() for s in f.readlines()]
		for s in strings:
			print(s)
		f.close

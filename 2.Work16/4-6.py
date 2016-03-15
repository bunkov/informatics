import argparse
import os

parser = argparse.ArgumentParser(
    description='analogue of utility "tree"'
)

parser.add_argument(
    'way',
    metavar='WAY',
    help='...way'
)

parser.add_argument(
    '--folders-only',
    action='store_true',
    help='...folders only'
)

parser.add_argument(
    '--include',
    metavar='SOME_TEXT',
    action='store',
    help='show you files and folders, that'
)

parser.add_argument(
    '--exclude',
    metavar='SOME_TEXT',
    action='store',
    help='show you files and folders, that'
)

args = parser.parse_args()

way = args.way
'''if os.path.exists(way):
	print(os.listdir(path='.'))'''
if os.path.exists(way):
	directory = os.listdir(path = way)
	for i in range(len(directory)):
		if os.path.isfile(os.path.join(way, directory[i])):
			print(directory[i])
else:
	print('This way is not exists')

import argparse

parser = argparse.ArgumentParser(
	description='Console Calculator'
)

parser.add_argument(
	'values',
	metavar='VALUE',
	type=float,
	nargs=2,
	help='input data'
)

parser.add_argument(
	'-a',
	'--action',
	action='store',
	metavar='SYMBOL',
	help='help'
)

args = parser.parse_args()

values = args.values

if args.action is '+':
	print(values[0]+values[1])
elif args.action is '-':
	print(values[0]-values[1])
elif args.action is '*':
	print(values[0]*values[1])
elif args.action is '/':
	print(values[0]/values[1])

import argparse
import os

parser = argparse.ArgumentParser(
    description='analogue of utility "tree"'
)

# Позиционный обязательный параметр
parser.add_argument(
    'way',
    metavar='WAY',
    help='Путь'
)

# Опция (все опции (доп. возможности, лат. "свободный выбор") необязательны)
parser.add_argument(
    '--folders_only',
    action='store_true',
    help='Показывать только папки'
)

parser.add_argument(
    '--include',
    metavar='SOME_TEXT', # Название переменной, которая идет после - "мета" - опции
    action='store',
    help='Показывать только объекты, включающие в имени SOME_TEXT'
)

parser.add_argument(
    '--exclude',
    metavar='SOME_TEXT',
    action='store',
    help='Показывать только объекты, не содержащие в имени SOME_TEXT'
)

parser.add_argument(
    '--pretty',
    action='store_true',
    help='Показывать дерево по-крутому'
)

def deep_print(way, directory, pretty, folders_only, include, exclude, n = 0, s_arr = [], sign = ''):
	if folders_only:
		i = 0
		while i < len(directory):
			if os.path.isfile(os.path.join(way, directory[i])):
				directory.pop(i)
			else:
				i += 1
	if include:
		i = 0
		while i < len(directory):
			if include not in directory[i]:
				directory.pop(i)
			else:
				i += 1
	if exclude:
		i = 0
		while i < len(directory):
			if exclude in directory[i]:
				directory.pop(i)
			else:
				i += 1
	
	for i in range(len(directory)):
		for symbol in s_arr:
			sign += symbol
		if i+1 == len(directory): # Последний объект в директории
			sign += '╘'
			s_arr.append(' ')
		else:
			sign += '╞'
			s_arr.append('│')
		new_way = os.path.join(way, directory[i]) # Склеить путь и имя объекта через разделительный символ
		if pretty:
			print(sign, directory[i], sep = '')
		else:
			print(' '*(n+1), directory[i], sep = '')
		if os.path.isdir(new_way): # Если папка
			new_directory = os.listdir(path = new_way) # Питоновский список файлов и папок, лежащих new_way
			n += 1 # Номер уровня погружения увеличивается
			deep_print(new_way, new_directory, pretty, folders_only, include, exclude, n, s_arr)
			n -= 1 # Вернулись на этот уровень
		s_arr.pop()
		sign = ''

args = parser.parse_args() # Объект с опциями и поз. параметрами в качестве атрибутов объекта

way = args.way

if os.path.exists(way): # Путь существует
	directory = os.listdir(path = way)
	deep_print(way, directory, args.pretty, args.folders_only, args.include, args.exclude)
else:
	print('Указанный путь не существует')
print('\n', chr(2), sep = '') # Смайл
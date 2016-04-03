import matplotlib.pyplot as plt
import networkx as nx

def get_graph(file_name = 'FruitLand'): # Считать граф из файла
	data_file = open(file_name + '.txt')
	G = nx.Graph() # Создать пустой граф
	edges_num = int(data_file.readline().rstrip()) # Кол-во ребер (указано в начале файла)
	data = [0]*edges_num # Массив строк ('вершина вершина вес')
	for i in range (edges_num):
		data[i] = data_file.readline().rstrip().split()
		vertex_1 = data[i][0]
		if len(data[i]) == 1 and vertex_1 not in G: # Если в строке изолированная вершина и ее нет в графе
			G.add_node(vertex_1) # Добавить в граф вершину
		else:
			vertex_2 = data[i][1]
			if len(data[i]) == 3: # Если в строке есть вес - третье значение
				w = data[i][2]
			else:
				w = 1
			G.add_edge(vertex_1, vertex_2, weight = w) # Добавить в граф ребро
	data_file.close()
	return G

def rendering(G): # Отрисовка и возврат координат
	pos = nx.spring_layout(G) # Задать координаты вершин графа по методу spring
	
	# Отрисовываем весь граф
	nx.draw_networkx_nodes(G,pos,node_size=100)
	nx.draw_networkx_edges(G, pos, G.edges(), width=5, alpha=1, edge_color='b')
	nx.draw_networkx_labels(G,pos,font_size=20,font_family='arial')
	return pos

def get_path(G): # Считать по вводимым данным путь в графе
	length = int(input('Длина пути: '))
	edge_list = [0]*length # Массив ребер пути (возвращается для отрисовки этих ребер)
	print('Номер ребра: <вершина 1> ' ' <вершина 2>')
	i = 0 # Номер ребра минус один
	while i < (length): # Пока меньше длины пути минус один
		print(i+1, end = ': ')
		edge_list[i] = input().split() # Элемент массива - кортеж вершин
		vertex_1 = edge_list[i][0]
		vertex_2 = edge_list[i][1]
		if (vertex_1 not in G.nodes() or vertex_2 not in G.nodes() # Если вершин нет в графе
			or (i != 0 and edge_list[i-1][1] != vertex_1) # Если конец пройденного ребра не начало нового
			or (vertex_1, vertex_2) not in G.edges() and (vertex_2, vertex_1) not in G.edges()): # Нет такого ребра
				print("Ошибка: не путь")
				i -= 1 # Для повторного ввода
		i += 1
	return edge_list

if __name__ == '__main__':
	G = get_graph('NumberLand')
	nx.draw_networkx_edges(G, rendering(G), get_path(G), width=6, alpha=1, edge_color='r') # Отрисовываем путь

	plt.axis('off')
	plt.show()
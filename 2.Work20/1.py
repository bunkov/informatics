import matplotlib.pyplot as plt
import networkx as nx

def get_graph(data_file):
	G = nx.Graph()
	edges_num = int(data_file.readline().rstrip())
	data = [0]*edges_num
	for i in range (edges_num):
		data[i] = data_file.readline().rstrip().split()
		vertex_1 = data[i][0]
		if len(data[i]) == 1 and vertex_1 not in G:
			G.add_node(vertex_1)
		else:
			vertex_2 = data[i][1]
			if len(data[i]) == 3:
				w = data[i][2]
			else:
				w = 1
			G.add_edge(vertex_1, vertex_2, weight = w)
	return G

def get_path(G):
	length = int(input('Length of path: '))
	edge_list = [0]*length
	print('edge(vertex 1, vertex 2):')
	i = 0
	while i < (length):
		print(i+1, end = ': ')
		edge_list[i] = input().split()
		if (edge_list[i][0] not in G.nodes() or edge_list[i][1] not in G.nodes() # Если вершин нет в графе
			or (i != 0 and edge_list[i-1][1] != edge_list[i][0]) # Если конец пройденного ребра не начало нового
			or (edge_list[i][0], edge_list[i][1]) not in G.edges() and (edge_list[i][1], edge_list[i][0]) not in G.edges()): # Нет такого ребра
				print("It isn't path")
				i -= 1
		i += 1
	return edge_list

def dfs(G, start, called = [], edge_list = []): # Поиск по глубине
	called.append(start)
	for neighbour in G[start]:
		if neighbour not in called:
			dfs(G, neighbour, called, edge_list)
			edge = (start, neighbour)
			edge_list.append(edge)
	return edge_list, called

def bfs(G, start, fired = [], edge_list= []): # Поиск по ширине
	queue = [start]
	fired.append(start)
	while queue:
		current = queue.pop(0)
		for neighbour in G[current]:
			if neighbour not in fired:
				fired.append(neighbour)
				queue.append(neighbour)
				edge = (current, neighbour)
				edge_list.append(edge)
	return edge_list, fired

def dijkstra(G, start): # Алгоритм дейкстры
	shortest_path = {node: float('+inf') for node in G}
	shortest_path[start] = 0
	queue = [start]
	while queue:
		current = queue.pop(0)
		for neighbour in G[current]:
			offered_shortest_path = shortest_path[current] + int(G[current][neighbour]['weight'])
			if offered_shortest_path < shortest_path[neighbour]:
				shortest_path[neighbour] = offered_shortest_path
				queue.append(neighbour)
	return shortest_path

data_file = open('2.txt')
#data_file = open(input('Name of file: ')+'.txt')
G = get_graph(data_file)
pos = nx.spring_layout(G)

# Отрисовываем весь граф
nx.draw_networkx_nodes(G,pos,node_size=100)
nx.draw_networkx_edges(G, pos, G.edges(), width=5, alpha=1, edge_color='b')
nx.draw_networkx_labels(G,pos,font_size=20,font_family='arial')

edge_list, woken = bfs(G, 'Апельсиновый') # Ребра основного дерева
n = 1 # Кол-во компонент связности
while len(woken) != len(G.nodes()):
	for node in G.nodes():
		if node not in woken:
			edge_part, woken_part = dfs(G, node)
			edge_list += edge_part
			woken += woken_part
			n += 1

#nx.draw_networkx_edges(G, pos, get_path(G), width=6, alpha=1, edge_color='r') # Отрисовываем путь
nx.draw_networkx_edges(G, pos, edge_list, width=8, alpha=0.5, edge_color='g') # Отрисовываем основное дерево
print('Кол-во компонент связности:', n)
if n == 1:
	print('Граф связный')
else:
	print('Граф несвязный')
town = input('The shortest path from: ')
print(dijkstra(G, town))
plt.axis('off')
plt.show()
data_file.close()
import matplotlib.pyplot as plt
import networkx as nx
import getter

def dfs(G, start, called = [], edge_list = []): # Поиск по глубине
	# Аргументы: граф, стартовая вершина, массив пройденных вершин, массив ребер
	called.append(start)
	for neighbour in G[start]: # Для соседа стартовой вершины 
		if neighbour not in called: # Сосед не пройден
			dfs(G, neighbour, called, edge_list) # В качестве стартовой - сосед
			edge = (start, neighbour) # Ребро - кортеж вершины и ее соседа
			edge_list.append(edge)
	return edge_list, called # Вернуть первый для дальнейшей отрисовки, второй для проверки связности

G = getter.get_graph()

edge_list, woken = dfs(G, 'Апельсиновый') # Ребра основного дерева и список пройденных вершин
n = 1 # Кол-во компонент связности
while len(woken) != len(G.nodes()): # Пока не все вершины пройдены
	for node in G.nodes():
		if node not in woken:
			edge_part, woken_part = dfs(G, node, [], []) # Часть ребер и вершин, которые не были пройдены ранее
			# По идее функция должна вызываться по умолчанию с пустыми массивами, но почему-то запоминает прежние значения
			edge_list += edge_part
			woken += woken_part
			n += 1

print('Кол-во компонент связности:', n)
if n == 1:
	print('Граф связный')
else:
	print('Граф несвязный')

nx.draw_networkx_edges(G, getter.rendering(G), edge_list, width=8, alpha=0.5, edge_color='g') # Отрисовываем основное дерево

plt.axis('off')
plt.show()
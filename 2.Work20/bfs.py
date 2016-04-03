import matplotlib.pyplot as plt
import networkx as nx
import getter

def bfs(G, start, fired = [], edge_list= []): # Поиск по ширине
	# Аргументы: граф, стартовая вершина, массив пройденных вершин, массив ребер
	queue = [start]
	fired.append(start)
	while queue: # Пока очередь не пуста
		current = queue.pop(0) # Взять первую в очереди вершину на обработку
		for neighbour in G[current]: # Для соседа этой вершины
			if neighbour not in fired: # Если он не пройден
				fired.append(neighbour)
				queue.append(neighbour)
				edge = (current, neighbour) # Ребро - кортеж вершины и ее соседа
				edge_list.append(edge)
	return edge_list, fired # Вернуть первый для дальнейшей отрисовки, второй для проверки связности

G = getter.get_graph()

edge_list, woken = bfs(G, 'Апельсиновый') # Ребра основного дерева и список пройденных вершин
n = 1 # Кол-во компонент связности
while len(woken) != len(G.nodes()): # Пока не все вершины пройдены
	for node in G.nodes():
		if node not in woken:
			edge_part, woken_part = bfs(G, node, [], []) # Часть ребер и вершин, которые не были пройдены ранее
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
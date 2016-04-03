import matplotlib.pyplot as plt
import networkx as nx
import getter
import dijkstra as d

G = getter.get_graph()
short_paths_list = {}
for node in G.nodes():
	short_paths_list[node] = d.dijkstra(G,node)
town_1 = input('Ищем кратчайший путь от ')
town_2 = input('до ')
current = town_2
edge_list = [] # Массив ребер кратчайшего пути (для отрисовки этих ребер)
while current != town_1:
	for neighbour in G[current]:
		path_to_current = short_paths_list[town_1][current]
		path_to_neighbour = short_paths_list[town_1][neighbour]
		weight = int(G[current][neighbour]['weight'])
		if path_to_current - path_to_neighbour == weight:
			edge_list.append((current, neighbour))
			current = neighbour
			break
	if current == town_2:
		print('Пути не существует')
		break

nx.draw_networkx_edges(G, getter.rendering(G), edge_list, width=6, alpha=1, edge_color='r') # Отрисовываем кратчайший путь

plt.axis('off')
plt.show()
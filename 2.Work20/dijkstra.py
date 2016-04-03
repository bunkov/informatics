import getter

def dijkstra(G, start): # Алгоритм дейкстры
	shortest_path = {node: float('+inf') for node in G} # Кратчайший путь до каждой вершины - бесконечность
	shortest_path[start] = 0 # Для стартовой - ноль
	queue = [start]
	while queue: # Пока очередь не пуста
		current = queue.pop(0) # Взять первую в очереди вершину на обработку
		for neighbour in G[current]: # Для соседа этой вершины
			weight = int(G[current][neighbour]['weight']) # вес ребра меж обрабатываемой и соседом
			offered_shortest_path = shortest_path[current] + weight # возможно кратчайший путь = кратчайший до обрабатываемой + вес ребра
			if offered_shortest_path < shortest_path[neighbour]:
				shortest_path[neighbour] = offered_shortest_path
				queue.append(neighbour)
	return shortest_path

def main():
	town = input('Ищем кратчайший путь от: ') # Стартовая вершина
	if town in G.nodes():
		print(dijkstra(G, town))
	else:
		print('Ошибка: не город')
		main()

if __name__ == '__main__':
	G = getter.get_graph()
	main()
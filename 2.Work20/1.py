import matplotlib.pyplot as plt
import networkx as nx

def get_graph(data_file):
	G = nx.Graph()
	#vertices_num = int(input('Number of vertices'))
	edges_num = int(input('Numbers of edges: '))
	data = [0]*edges_num
	#for i in range (nodes_num):
		
	for i in range (edges_num):
		data[i] = data_file.readline().rstrip()
		vertex_1 = data[i][0]

		if len(data[i]) == 1:
			if vertex_1 not in G:
				G.add_node(vertex_1)
		elif len(data[i]) == 3:
			vertex_2 = data[i][2]
			G.add_edge(vertex_1, vertex_2, weight = 1)
		elif len(data[i]) == 5:
			w = data[i][4]
			vertex_2 = data[i][2]
			G.add_edge(vertex_1, vertex_2, weight = w)
	return G

def get_path():
	length = int(input('Length of path: '))
	edge_list = [0]*length
	print('edge(vertex 1, vertex 2): ')
	i = 0
	while i < (length):
		print(i+1, end = ': ')
		edge_list[i] = input().split()
		if i != 0:
			if edge_list[i-1][1] !=	edge_list[i][0]:
				print("It isn't path")
				i -= 1
		i += 1
	return edge_list
		
data_file = open(input('Name of file: ')+'.txt')
G = get_graph(data_file)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G,pos,node_size=700)
nx.draw_networkx_edges(G, pos, G.edges(), width=8, alpha=1, edge_color='b')
nx.draw_networkx_edges(G, pos, get_path(), width=8, alpha=1, edge_color='r')
nx.draw_networkx_labels(G,pos,font_size=20,font_family='sans-serif')
plt.axis('off')
plt.show()
data_file.close()

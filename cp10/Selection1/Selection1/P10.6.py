
from queue import Queue

vertex = [ 'A', 'B', 'C', 'D', 'E', 'F','G', 'H' ]
adjMat = [[ 0, 1, 1, 0, 0, 0, 0, 0 ],
		  [ 1, 0, 0, 1, 0, 0, 0, 0 ],
		  [ 1, 0, 0, 1, 1, 0, 0, 0 ],
		  [ 0, 1, 1, 0, 0, 1, 0, 0 ],
		  [ 0, 0, 1, 0, 0, 0, 1, 1 ],
		  [ 0, 0, 0, 1, 0, 0, 0, 0 ],
		  [ 0, 0, 0, 0, 1, 0, 0, 1 ],
		  [ 0, 0, 0, 0, 1, 0, 1, 0 ]]



def bfs_cc(adj, vtx, color, s, visited):
	visited[s] = True
	que = Queue()
	que.put(s)
	color.append(s)

	while not que.empty():
		now_vtx = que.get()

		for i in range(len(vtx)):
			if adj[now_vtx][i] == 1 and visited[i] != True:
				visited[i] = True
				que.put(i)
				if i not in color:
					color.append(i)
	return color


def find_connected_component(adj, vtx):
	n = len(vtx)
	visited = [False] * n
	colorList = []

	for i in range(len(vtx)):
		if visited[i] != True:
			color = bfs_cc(adj, vtx, [], i, visited)
			colorList.append(color)

	return colorList


def find_bridges(adj, vtx):
	n = len(vtx)
	count = 0
	visited = []

	for i in range(n):
		for j in range(n):
			if adj[i][j] != 0:
				adj[i][j] = adj[j][i] = 0
				if len(find_connected_component(adj, vtx)) > 1 and (i, j) not in visited:
					count += 1
					print("Bridge %d: (%s, %s)" % (count, vtx[i], vtx[j]))
					visited.append((i, j))
					visited.append((j, i))
				adj[i][j] = adj[j][i] = 1



print("find_bridge : ")
find_bridges(adjMat, vertex)
print()
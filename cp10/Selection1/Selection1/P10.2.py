
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


# ------------- 깊이우선탐색 ------------------
def dfs(adj, vtx, s):									
	n = len(vtx)
	visited = [False] * n
	dfs_recur(adj, vtx, visited, s)


def dfs_recur(adj, vtx, visited, id):
	visited[id] = True

	for i in range(len(vtx)):
		if adj[id][i] == 1 and visited[i] != True:
			print("%s " % vtx[i], end = '')
			dfs_recur(adj, vtx, visited, i)



# ------------- 너비우선탐색 ------------------
def bfs(adj, vtx, s):
	visited = [False] * len(vtx)
	visited[s] = True
	que = Queue()
	que.put(s)

	while not que.empty():
		now_vtx = que.get()
		print("%s " % vtx[now_vtx], end = '')

		for i in range(len(vtx)):
			if adj[now_vtx][i] == 1 and visited[i] != True:
				visited[i] = True
				que.put(i)


print("깊이우선탐색(DFS) : A ", end = '')
dfs(adjMat, vertex, 0)
print()
print("너비우선탐색(BFS) : ", end = '')
bfs(adjMat, vertex, 0)
print()
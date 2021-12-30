
import heapq

parent = []
set_size = 0

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[None, 29, None, None, None, 10, None],
		  [29, None, 16, None, None, None, 15],
		  [None, 16, None, 12, None, None, None],
		  [None, None, 12, None, 22, None, 18],
		  [None, None, None, 22, None, 27, 25],
		  [10, None, None, None, 27, None, None],
		  [None, 15, None, 18, 25, None, None]]


def init_set(nSets):
	global set_size, parent
	set_size = nSets
	for i in range(nSets):
		parent.append(-1)

def find(id):
	while (parent[id] >= 0):
		id = parent[id]
	return id

def union(s1, s2):
	global set_size
	parent[s1] = s2
	set_size = set_size - 1


def MSTKruskal(vertex, adj):
	vsize = len(vertex)
	init_set(vsize)
	eList = []

	for i in range(vsize-1):
		for j in range(i+1, vsize):
			if adj[i][j] != None:
				heapq.heappush(eList, (adj[i][j], i, j))

	edgeAccepted = 0
	while (edgeAccepted < vsize - 1):
		e = heapq.heappop(eList)
		uset = find(e[1])
		vset = find(e[2])

		if uset != vset:
			print("간선 추가 : (%s, %s, %d)" % (vertex[e[1]], vertex[e[2]], e[0]))
			union(uset, vset)
			edgeAccepted += 1

print("MST Krusal's Algorithm(최소 힙 사용)")
MSTKruskal(vertex, weight)
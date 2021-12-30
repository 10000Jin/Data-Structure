class Queue:
	def __init__(self):
		self._Items = list()

	def isEmpty(self):
		return len(self._Items) == 0

	def enqueue(self, item):
		self._Items.append(item)

	def dequeue(self):
		if not self.isEmpty():
			return self._Items.pop(0)

	def peek(self):
		if not self.isEmpty(): 
			return self._Items[-1]


map = [ ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'], 
	   ['1', '1', '0', '0', '0', '1', '0', '0', '0', 'x'], 
	   ['1', '1', '1', '0', '1', '1', '0', '1', '1', '1'],
	   ['1', '1', '1', '0', '1', '0', '0', '1', '1', '1'],
	   ['e', '0', '0', '0', '1', '1', '0', '0', '0', '1'],
	   ['1', '0', '1', '0', '1', '1', '1', '1', '0', '1'],
	   ['1', '0', '1', '0', '1', '1', '0', '0', '0', '1'],
	   ['0', '0', '1', '0', '1', '1', '0', '1', '0', '1'],
	   ['1', '1', '1', '0', '0', '0', '0', '1', '1', '1'],
	   ['1', '1', '1', '1', '1', '1', '1', '1', '1', '1'] ]

MAZE_SIZE = 10

def isValidPos(x, y):
	if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
		return False
	else:
		return map[y][x] == '0' or map[y][x] == 'x'


def BFS():
	que = Queue()
	que.enqueue((0, 4))
	print('BFS: ')

	while not que.isEmpty():
		here = que.dequeue()
		print(here, end = ' -> ')
		x, y = here
		if(map[y][x] == 'x'):
			return True
		else:
			map[y][x] = '.'
			if isValidPos(x, y-1): que.enqueue((x, y-1))
			if isValidPos(x, y+1): que.enqueue((x, y+1))
			if isValidPos(x-1, y): que.enqueue((x-1, y))
			if isValidPos(x+1, y): que.enqueue((x+1, y))
	return False


result = BFS()
if result : print(' --> 미로탐색 성공')
else: print(' --> 미로탐색 실패')
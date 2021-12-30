
class Entry:
	def __init__(self, key, value):
		self.key = key
		self.value = value

	def __str__(self):
		return str("%s:%s" % (self.key, self.value))	

class LinearProbMap:
	def __init__(self, M):
		self.table = [None] * M
		self.M = M

	def hashFn(self, key):
		sum = 0
		for c in key:
			sum = sum + ord(c)
		return sum % self.M

	def insert(self, key, value):
		idx = self.hashFn(key)
		while True:
			if self.table[idx] == None or self.table[idx] == '.':
				self.table[idx] = Entry(key, value)
				break
			else:
				idx += 1
				if idx == 13:
					idx = 0

	def search(self, key):
		idx = self.hashFn(key)
		while not self.table[idx] == None:
			if self.table[idx] == '.':
				idx += 1
				if idx == 13:
					idx = 0
				continue
			if self.table[idx].key == key:
				return self.table[idx]
			else: 
				idx += 1
				if idx == 13:
					idx = 0
		return None

	def delete(self, key):
		idx = self.hashFn(key)
		while not self.table[idx] == None:
			if self.table[idx] == '.':
				idx += 1
				if idx == 13:
					idx = 0
				continue
			if self.table[idx].key == key:
				self.table[idx] = '.'
				break
			else:
				idx += 1
				if idx == 13:
					idx = 0

	def display(self, msg):
		print(msg)
		for idx in range(len(self.table)):
			print("[%2d] -> " % idx, self.table[idx])
				

map = LinearProbMap(13)
map.insert('data', '자료')
map.insert('structure', '구조')
map.insert('sequential search', '선형 탐색')
map.insert('game', '게임')
map.insert('binary search', '이진 탐색')
map.display("나의 단어장")

print()
print("탐색: game --> ", map.search('game'))
print("탐색: over --> ", map.search('over'))
print("탐색: data --> ", map.search('data'))
print()

map.delete('game')
map.display("game을 삭제한 나의 단어장")
print()

map.delete('binary search')
map.display("binary search을 삭제한 나의 단어장")

print()
print("탐색: game --> ", map.search('game'))
print("탐색: over --> ", map.search('over'))
print("탐색: data --> ", map.search('data'))
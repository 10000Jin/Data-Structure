
class Set:
	def __init__(self):
		self.items = []
	
	def size(self):
		return len(self.items)

	def display(self, msg):
		print(msg, self.items)
	
	def contains(self, item):
		return item in self.items


	def insert(self, elem):
		if elem in self.items: return
		for idx in range(len(self.items)):
			if elem < self.items[idx]:
				self.items.insert(idx, elem)
				return
		self.items.append(elem)

	def delete(self, elem):
		if elem in self.items:
			self.items.remove(elem)

	def __eq__(self, setB):
		if self.size() != setB.size():
			return False
		for idx in range(len(self.items)):
			if self.items[idx] != setB.items[idx]:
				return False
		return True

	def union(self, setB):
		newSet = Set()
		a = b = 0
		while a < len(self.items) and b < len(setB.items):
			valueA = self.items[a]
			valueB = setB.items[b]
			if valueA < valueB:
				newSet.items.append(valueA)
				a += 1
			elif valueA > valueB:
				newSet.items.append(valueB)
				b += 1
			else: 
				newSet.items.append(valueA)
				a += 1
				b += 1
		while a < len(self.items):
			newSet.items.append(self.items[a])
			a += 1
		while b > len(setB.items):
			newSet.items.append(self.items[b])
			b += 1
		return newSet

	def intersection(self, setB):
		newSet = Set()
		a = b = 0
		while a < len(self.items) and b < len(setB.items):
			valueA = self.items[a]
			valueB = setB.items[b]
			if valueA < valueB:
				a += 1
			elif valueA > valueB:
				b += 1
			else: 
				newSet.items.append(valueA)
				a += 1
				b += 1
		return newSet

	def difference(self, setB):
		newSet = Set()
		a = b = 0
		while a < len(self.items) and b < len(setB.items):
			valueA = self.items[a]
			valueB = setB.items[b]
			if valueA < valueB:
				newSet.items.append(valueA)
				a += 1
			elif valueA > valueB:
				b += 1
			else: 
				a += 1
				b += 1
		return newSet



setA = Set()
setA.insert("사과")
setA.insert("포도")
setA.insert("멜론")	
setA.insert("수박")
setA.insert("복숭아")
setA.display("set A = ")

setB = Set()
setB.insert("딸기")
setB.insert("참외")
setB.insert("포도")
setB.insert("키위")
setB.insert("사과")
setB.display("set B = ")

print("\n수정된 집합: ")

setA.insert("배")
setA.display("set A = ")
setB.delete("참외")
setB.display("set B = ")
print()

setA.union(setB).display("A ∪ B = ")
setA.intersection(setB).display("A ∩ B = ")
setA.difference(setB).display("A - B = ")

class Node:
	def __init__(self, elem, link = None):
		self.data = elem
		self.link = link

class LinkedList:
	def __init__(self):
		self.head = None
	def isEmpty(self): return self.head == None
	def clear(self): self.head = None
	def size(self): 
		node = self.head
		count = 0
		while not node == None:
			node = node.link
			count += 1
		return count
	def getNode(self, pos):         
		if pos < 0: return None
		node = self.head
		while pos > 0 and node != None:
			node = node.link
			pos -= 1
		return node
	def getEntry(self, pos):
		node = self.getNode(pos)
		if node == None: return None
		else: return enode.data
	def replace(self, pos, elem):
		node = self.getNode(pos)
		if node != None: node.data = elem
	def find(self, data):
		node = self.head
		while node is not None:
			if node.data == data: return node
			node = node.link
		return node
	def insert(self, pos, elem):
		before = self.getNode(pos-1)
		if before == None:
			self.head = Node(elem, self.head)
		else: 
			node = Node(elem, before.link)
			before.link = node
	def delete(self, pos):
		before = self.getNode(pos-1)
		if before == None:
			if self.head is not None:
				sefl.head = sefl.head.link
		elif before.link != None:
			before.link = before.link.link

class Term:
	def __init__(self, expo, coef):
		self.expo = expo
		self.coef = coef

class SparsePoly(LinkedList):
	def __init__(self):
		super().__init__()
	def degree(self):
		if self.head == None: return 0
		else: return self.head.data.expo
	def read(self):
		self.clear()
		token = input("입력(계수 차수 계수 차수 ... [엔터]): ").split(" ")
		for i in range(len(token)//2):
			self.insert(self.size(), Term(int(token[i*2+1]), int(token[i*2])))
	
	def add(self, x):
		a = SparsePoly()
		node1 = self.head
		node2 = x.head

		while not node1 == None and not node2 == None:
			if node1.data.expo == node2.data.expo:
				a.insert(a.size(), Term(node1.data.expo, node1.data.coef+node2.data.coef))
				node1 = node1.link
				node2 = node2.link
			elif node1.data.expo > node2.data.expo:
				a.insert(a.size(), Term(node1.data.expo, node1.data.coef))
				node1 = node1.link
			elif node1.data.expo < node2.data.expo:
				a.insert(a.size(), Term(node2.data.expo, node2.data.coef))
				node2 = node2.link

		while not node1 == None:
			a.insert(a.size(), Term(node1.data.expo, node1.data.coef))
			node1 = node1.link
		while not node2 == None:
			a.insert(a.size(), Term(node2.data.expo, node2.data.coef))
			node2 = node2.link
		return a

	def neg(self):
		n = SparsePoly()
		node = self.head
		while not node == None:
			n.insert(n.size(), Term(node.data.expo, -node.data.coef))
			node = node.link
		return n

	def sub(self, x):
		n = x.neg()
		s = self.add(n)
		return s
	
	def mul(self, x):
		m = SparsePoly()
		node1 = self.head
		node2 = x.head

		while not node1 == None:
			while not node2 == None:
				tmp = SparsePoly()
				tmp.insert(tmp.size(), Term(node1.data.expo + node2.data.expo, node1.data.coef * node2.data.coef))
				m = m.add(tmp)
				node2 = node2.link
			node1 = node1.link
			node2 = x.head
		return m

	def display(self, msg = ''):
		result = ''
		node = self.head
		for i in range(self.size()):
			if node.data.expo == 0:
				if node.data.coef > 0: result += "%d" % node.data.coef
				elif node.data.coef < 0: result += "\b\b%d" % node.data.coef
			elif node.data.expo == 1:
				if node.data.coef > 0: result += "%dx + " % node.data.coef
				elif node.data.coef < 0: result += "\b\b%dx + " % node.data.coef
			elif node.data.coef > 0 :
				result += "%dx^%d + " % (node.data.coef, node.data.expo)
			elif node.data.coef < 0 :
				result += "\b\b%dx^%d + " % (node.data.coef, node.data.expo)
			node = node.link
		print(msg, result)


a = SparsePoly()
b = SparsePoly()
a.read()
b.read()
c = a.add(b)
d = a.sub(b)
e = a.mul(b)

print("\n입력한 다항식 : ")
a.display("	A(x) = ")
b.display("	B(x) = ")

print("\n두 다항식의 합 : ")
c.display("	C(x) = ")
print("\n두 다항식의 차 : ")
d.display("	D(x) = ")
print("\n두 다항식의 곱 : ")
e.display("	D(x) = ")
print()

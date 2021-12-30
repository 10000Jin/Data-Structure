class Polynomial :
	def __init__(self) :
		self.coef = []

	def degree(self) : 
		return len(self.coef) - 1

	def evaluate(self, x) :
		eval = 0
		for i in range(len(self.coef)) :
			eval += self.coef[i] * x**i
		return eval
	
	def add(self, b) :
		y = Polynomial()
		if len(self.coef) > len(b.coef) :
			y.coef = self.coef.copy()
			for i in range(len(self.coef)) :
				y.coef[i] += b.coef[i]
				
		else :
			y.coef = b.coef.copy()
			for i in range(len(self.coef)) :
				y.coef[i] += self.coef[i]
		return y

	def negation(self) :
		for i in range(len(self.coef)) :
			self.coef[i] = self.coef[i] * -1

	def subtract(self, a) :
		a.negation()
		s = self.add(a)
		a.negation()
		return s

	def multiply(self, b) :
		z = Polynomial()
		z.coef = [0] * (len(self.coef) + len(b.coef) - 1)
		for i in range(len(self.coef)) :
			for j in range(len(b.coef)):
				z.coef[i+j] += self.coef[i] * b.coef[j]
		return z

	def display(self, msg = "f(x) = ") :
		full = ''
		for i in range(len(self.coef) - 1, -1, -1) :
			if self.coef[i] == 0 :
				continue
				
			if i == 0 :
				if self.coef[i] > 0 :
					full += "%d" % self.coef[i]
				elif self.coef[i] < 0 :
					full += "\b\b%d" % self.coef[i]
			elif i == 1 :
				if self.coef[i] > 0 :
					full += "%dx + " % self.coef[i]
				elif self.coef[i] < 0 :
					full += "\b\b%dx + " % self.coef[i]
			elif self.coef[i] > 0 :
				full += "%dx^%d + " % (self.coef[i], i)
			elif self.coef[i] < 0 :
				full += "\b\b%dx^%d + " % (self.coef[i], i)
		print(msg, full)



#def read_poly() :
#	p = Polynomial()
#	deg = int(input("다항식의 최고 차수를 입력하시오. : "))
#	for n in range(deg+1) : 
#		coef = float(input("	x^%d의 계수 : " % (deg-n)))
#		p.coef.append(coef)
#	p.coef.reverse()
#	return p

def read_poly() :
	p = Polynomial()
	deg = list(map(float, input("다항식의 계수를 순서대로 입력하시오. :  ").split()))
	for i in range(len(deg)) :
		coef = deg[i]
		p.coef.append(coef)
	p.coef.reverse()
	return p



a = read_poly()
b = read_poly()
c = a.add(b)
d = a.subtract(b)
e = a.multiply(b)

print("입력한 다항식 : ")
a.display("	A(x) = ")
b.display("	B(x) = ")

print("\n두 다항식의 합 : ")
c.display("	C(x) = ")
print("\n두 다항식의 차 : ")
d.display("	D(x) = ")
print("\n두 다항식의 곱 : ")
e.display("	E(x) = ")
print()

print("A(5) = ", a.evaluate(5))
print("A(2) = ", a.evaluate(2))
print("B(5) = ", b.evaluate(5))
print("B(2) = ", b.evaluate(2))
print("C(5) = ", c.evaluate(5))
print("C(2) = ", c.evaluate(2))
print("D(5) = ", d.evaluate(5))
print("D(2) = ", d.evaluate(2))
print("E(5) = ", e.evaluate(5))
print("E(2) = ", e.evaluate(2))
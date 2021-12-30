
class Stack:
	def __init__(self):
		self._Items = list()

	def isEmpty(self):
		return len(self._Items) == 0

	def push(self, item):
		self._Items.append(item)

	def peek(self):
		if not self.isEmpty():
			return self._Item[-1]

	def pop(self):
		if not self.isEmpty():
			return self._Items.pop()


def checkBrackets(statment):
	stack = Stack()
	for ch in statement:
		if ch in ('{', '[', '('):
			stack.push(ch)
		elif ch in ('}', ']', ')'):
			if stack.isEmpty():
				return False
			else :
				left = stack.pop()
				if (ch == "}" and left != "{") or \
					(ch == "]" and left != "[") or \
					(ch == ")" and left != "(") :
					return False

	return stack.isEmpty()



def isValidSource(srcfile):
	stack = Stack()
	nLine = nChar = check = count = 0
	
	for line in srcfile:
		nLine += 1
		for ch in line:
			nChar += 1
			if ch == "\'":
				check = 1
			elif ch == "\'" and check == 1:
				check = 0
			
			if ch == "\"":
				check = 2
			elif ch == "\"" and check == 2:
				check = 0

			if ch == "/":
				count += 1
				continue
			if count == 2:
				check = 3
			if ch == "\n" and check == 3:
				check = 0

			if ch in ('{', '[', '('):
				if check == 0:
					stack.push(ch)
			elif ch in ('}', ']', ')'):
				if check == 0:
					if stack.isEmpty():
						return 2, nLine, nChar
					else :
						left = stack.pop()
						if (ch == "}" and left != "{") or \
							(ch == "]" and left != "[") or \
							(ch == ")" and left != "(") :
							return 3, nLine, nChar

	if stack.isEmpty() == False: 
		return 1, nLine, nChar

	return 0, nLine, nChar


	
#filename = "ArrayStack.h"
filename = "CheckBracketMain.cpp"

infile = open(filename, "r")
lines = infile.readlines();
infile.close()

eCode, lcnt, ccnt = isValidSource(lines)
print(filename, " ---> ", eCode)
print(" 라인수 = ", lcnt)
print(" 문자수 = ", ccnt)
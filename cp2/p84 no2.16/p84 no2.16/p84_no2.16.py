def printNum(n) :
	print("%3d" % (11 - n), end = ' ')
	if n > 1  :
		printNum(n - 1)


def printRevNum(n) : 
	print("%3d" % n, end = ' ')
	n -= 1
	if n > 0 :
		printRevNum(n)

printNum(10)
print()
printRevNum(10)
print()

# print함수에는 줄바꿈 계행 문자가 포함되어 있음
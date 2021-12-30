def fib(n) :
	if n == 0 : return 0
	elif n == 1 : return 1
	else : 
		return fib(n - 1) + fib(n - 2)

def fib_iter(n) :
	if (n < 2) : return n

	last = 0
	current = 1
	for i in range(2, n + 1) :
		tmp = current
		current += last
		last = tmp
	return current

print('Fibonacci반복(5) = ', fib(5))
print('Fibonacci순환(5) = ', fib_iter(5), '\n')
print('Fibonacci반복(7) = ', fib(7))
print('Fibonacci순환(7) = ', fib_iter(7), '\n')

import time

for i in range(1,40) :
	start = time.time()
	fib_iter(i)
	end = time.time()

	start2 = time.time()
	fib(i)
	end2 = time.time()

	print('n= ', i, '반복: ', end-start, '순환: ', end2-start2)
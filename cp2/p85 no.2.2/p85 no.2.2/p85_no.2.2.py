import random

answer = random.randint(0,99)
min = 0
max = 99
count = 0

for i in range(10) :
	guess = int(input("숫자를 입력하시오.(범위 : %d~%d) : " % (min, max)))
	count += 1

	if answer < guess :
		print("아닙니다. 더 작은 수 입니다!")
		max = guess
	
	elif answer > guess :
		print("아닙니다. 더 큰 수 입니다!")
		min = guess

	else :
		print("정답입니다!!!")
		print(count, "번 만에 맞추셨습니다!\n게임이 끝났습니다!")
		break
	



# guess = int(input("숫자를 입력하시오.(범위 : ", min, "~", max, ") : "))  안됌
# guess = int(input("숫자를 입력하시오.(범위 : %d~%d) : " % (min, max)))
# guess = int(input("숫자를 입력하시오.(범위 : " + str(min) + "~" + str(max) + ") :"))
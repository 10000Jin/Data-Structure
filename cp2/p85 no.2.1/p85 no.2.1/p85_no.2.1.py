income = input("소득을 입력하시오. (만원) ")

if int(income) <= 1200 : 
	tax = int(income) * 0.06
	after_income = int(income) - tax
	print("전체 세금 : ", tax, "만원\n순수 소득 : ", after_income, "만원 입니다.")

elif int(income) <= 4600 :
	tax = 1200 * 0.06 + (int(income) - 1200) * 0.15
	after_income = int(income) - tax
	print("전체 세금 : ", tax, "만원\n순수 소득 : ", after_income, "만원 입니다.")
		
elif int(income) <= 8800 : 
	tax = 1200 * 0.06 + 3400 * 0.15 + (int(income) - 4600) * 0.24
	after_income = int(income) - tax
	print("전체 세금 : ", tax, "만원\n순수 소득 : ", after_income, "만원 입니다.")

elif int(income) <= 15000 : 
	tax = 1200 * 0.06 + 3400 * 0.15 + 4200 * 0.24 +(int(income) - 8800) * 0.35
	after_income = int(income) - tax
	print("전체 세금 : ", tax, "만원\n순수 소득 : ", after_income, "만원 입니다.")

elif int(income) > 15000 : 
	tax = 1200 * 0.06 + 3400 * 0.15 + 4200 * 0.24 + 6200 * 0.35 + (int(income) - 15000) * 0.38
	after_income = int(income) - tax
	print("전체 세금 : ", tax, "만원\n순수 소득 : ", after_income, "만원 입니다.")


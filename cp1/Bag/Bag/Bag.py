
def contains(bag, e):						
	return e in bag							

def insert(bag, e):
	bag.append(e)

def remove(bag, e):
	bag.remove(e)

def count(bag):
	return len(bag)

def numOf(bag, e):
	count = 0
	for i in range(len(bag)):
		if bag[i] == e:
			count = count + 1
	return count


mybag = []
insert(mybag, '휴대폰')
insert(mybag, '지갑')
insert(mybag, '손수건')
insert(mybag, '빗')
insert(mybag, '자료구조')
insert(mybag, '야구공')
print('가방속의 물건', mybag)

remove(mybag, '휴대폰')
remove(mybag, '손수건')
insert(mybag, '손수건')
print('가방속의 물건', mybag)

print('빗의 개수', numOf(mybag, '빗'))
print('휴대폰의 개수', numOf(mybag, '휴대폰'))
print('축구공의 개수', numOf(mybag, '축구공'))
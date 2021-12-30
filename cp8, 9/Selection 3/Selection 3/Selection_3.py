
# --------------------------- 모스 코드표  ----------------------------------

table = [ ('ㄱ', '.-..'), ('ㄴ', '..-.'), ('ㄷ', '-...'), ('ㄹ', '...-'), ('ㅁ', '--'), ('ㅂ', '.--'), 
		 ('ㅅ', '--.'), ('ㅇ', '-.-'), ('ㅈ', '.--.'), ('ㅊ', '-.-.'), ('ㅋ', '-..-'), ('ㅌ', '--..'), ('ㅍ', '---'), 
	   ('ㅎ', '.---'), ('ㅏ', '.'), ('ㅑ', '..'), ('ㅓ', '-'), ('ㅕ', '...'), ('ㅗ', '.-'), ('ㅛ', '-.'), ('ㅜ', '....'),
	   ('ㅠ', '.-.'), ('ㅡ', '-..'), ('ㅣ', '..-'), ('ㅔ', '-.--'), ('ㅐ', '--.-'), ('1', '.----'), ('2', '..---'), ('3', '...--'),
	  ('4', '....-'), ('5', '.....'), ('6', '-....'), ('7', '--...'), ('8', '---..'), ('9', '----.'), ('0', '-----'), (' ', ' '), ('.', '.-.-.-'), 
	   (',', '--..--'), ('(', '-.--.'), (')', '-.--.-'), ('?', '..--..') ]

# ------------------------ 초, 중, 종성 테이블 -------------------------

Chosung = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ',  'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ',
		  'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
Jungsung = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ',
		   'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
Jongsung = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ',
		   'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ'] 


class TNode:
	def __init__(self, data, left, right):
		self.data = data
		self.left = left
		self.right = right

def make_morse_tree():
	root = TNode(None, None, None)
	for tp in table:
		code = tp[1]
		node = root
		for c in code:
			if c == '.':
				if node.left == None:
					node.left = TNode(None, None, None)
				node = node.left
			elif c == '-':
				if node.right == None:
					node.right = TNode(None, None, None)
				node = node.right

		node.data = tp[0]
	return root

def decode(root, code):									# 디코딩
	node = root
	for c in code:										 
		if c == '.' : node = node.left					# '.'이면 왼쪽 노드 이동
		elif c == '-' : node = node.right				# '-'이면 오른쪽 노드 이동
	return node.data

def encode(ch):											# 인코딩
	for i in range(len(table)):
		if ch == table[i][0] : return table[i][1]		# 해당 문자의 모스 코드 반환
	else:
		a, b =  DoubleWord2Word(ch)						# 테이블에 없다면 이중문자 -> 단일문자로 분해
		x = encode(a)									# 두 단일문자를 다시 인코딩 
		y = encode(b)
		return x, y										# 두 단일문자의 모스 코드 튜플형태로 반환




def Complete2Combination(Complete):								# 완성형을 조합형으로
	Combination_list = []										# 조합형 문자를 저장할 리스트
	for c in list(Complete):
		if c >= '가' and c <= '힣':								# 한글일 경우에
			ch = ord(c) - 44032
			cho = ch // (21 * 28)								# 초성 값 추출
			Combination_list.append(Chosung[cho])				# 초성 테이블에 해당하는 문자를 추가
			jung = (ch // 28) % 21								# 중성 값 추출
			Combination_list.append(Jungsung[jung])
			jong = ch % 28										# 종성 값 추출
			Combination_list.append(Jongsung[jong])
		else:													# 한글이 아니라면 (숫자, 특수문자)
			Combination_list.append(c)							# 문자를 바로 추가

	return Combination_list										# 조합형으로 분리된 문자 리스트 반환


def Combination2Complete(lst):									# 조합형을 완성형으로 
	count = 0													# 초, 중, 종성 자리를 나타낼 변수
	result = []													# 완성형 문자들을 저장할 리스트
	
	for i in range(len(lst)):
		if lst[i] not in Chosung and lst[i] not in Jungsung and lst[i] not in Jongsung:		# 초, 중, 종성 테이블에 없다면
			result.append(lst[i])								# result에 바로 추가 (count 증가x)
		else:													# 테이블에 있다면
			if count % 3 == 0:									# count가 3배수 즉 초성자리이면
				F = lst[i]										# 해당문자를 F에 저장
				count += 1										# 그리고 count 1증가
			elif count % 3 == 1:								# count가 3배수+1 즉 중성자리이면
				S = lst[i]
				count += 1
			elif count % 3 == 2:								# count가 3배수+2 즉 종성자리이면
				T = lst[i]
				count += 1
			if count != 0 and count % 3 == 0:					# 첫번째 문자의 초성이 아닌 초성자리에 오면
				result.append(chr((((Chosung.index(F) * 21) + Jungsung.index(S)) * 28) + Jongsung.index(T) + 44032))
																# 완성형 문자로 만들어 result에 추가
	return result


def DoubleWord2Word(ch):
	if ch == 'ㄲ':
		return 'ㄱ', 'ㄱ'
	elif ch == 'ㄸ':
		return 'ㄷ', 'ㄷ'
	elif ch == 'ㅃ':
		return 'ㅂ', 'ㅂ'
	elif ch == 'ㅆ':
		return 'ㅅ', 'ㅅ'
	elif ch == 'ㅉ':
		return 'ㅈ', 'ㅈ'
	elif ch == 'ㅖ':
		return 'ㅕ', 'ㅣ'
	elif ch == 'ㅒ':
		return 'ㅑ', 'ㅣ'
	elif ch == 'ㅘ':
		return 'ㅗ', 'ㅏ'
	elif ch == 'ㅙ':
		return 'ㅗ', 'ㅐ'
	elif ch == 'ㅚ':
		return 'ㅗ', 'ㅣ'
	elif ch == 'ㅝ':
	    return 'ㅜ', 'ㅓ'
	elif ch == 'ㅞ':
		return 'ㅜ', 'ㅔ'
	elif ch == 'ㅟ':
		return 'ㅜ', 'ㅣ'
	elif ch == 'ㅢ':
		return 'ㅡ', 'ㅣ'
	elif ch == 'ㄳ':
		return 'ㄱ', 'ㅅ'
	elif ch == 'ㄵ':
		return 'ㄴ', 'ㅈ'
	elif ch == 'ㄶ':
		return 'ㄴ', 'ㅎ'
	elif ch == 'ㄺ':
		return 'ㄹ', 'ㄱ'
	elif ch == 'ㄻ':
		return 'ㄹ', 'ㅁ'
	elif ch == 'ㄼ':
		return 'ㄹ', 'ㅂ'
	elif ch == 'ㄽ':
		return 'ㄹ', 'ㅅ'
	elif ch == 'ㄾ':
		return 'ㄹ', 'ㅌ'
	elif ch == 'ㄿ':
		return 'ㄹ', 'ㅍ'
	elif ch == 'ㅀ':
		return 'ㄹ', 'ㅎ'
	elif ch == 'ㅄ':
		return 'ㅂ', 'ㅅ'										# 이중문자를 단일문자들로 분리

def Word2DoubleWord(a, b):
	if a == 'ㄱ' and b == 'ㄱ':
		return 'ㄲ'
	elif a == 'ㄷ' and b == 'ㄷ':
		return 'ㄸ'
	elif a == 'ㅂ' and b == 'ㅂ':
		return 'ㅃ'
	elif a == 'ㅅ' and b == 'ㅅ':
		return 'ㅆ'
	elif a == 'ㅈ' and b == 'ㅈ':
		return 'ㅉ'
	elif a == 'ㅕ' and b == 'l':
		return 'ㅖ'
	elif a == 'ㅑ' and b == 'ㅣ':
		return 'ㅒ'
	elif a == 'ㅗ' and b == 'ㅏ':
		return 'ㅘ'
	elif a == 'ㅗ' and b == 'ㅐ':
		return 'ㅙ'
	elif a == 'ㅗ' and b == 'ㅣ':
		return 'ㅚ'
	elif a == 'ㅜ' and b == 'ㅓ':
		return 'ㅝ'
	elif a == 'ㅜ' and b == 'ㅔ':
		return 'ㅞ'
	elif a == 'ㅜ' and b == 'ㅣ':
		return 'ㅟ'
	elif a == 'ㅡ' and b == 'ㅣ':
		return 'ㅢ'
	elif a == 'ㄱ' and b == 'ㅅ':
		return 'ㄳ'
	elif a == 'ㄴ' and b == 'ㅈ':
		return 'ㄵ'
	elif a == 'ㄴ' and b == 'ㅎ':
		return 'ㄶ'
	elif a == 'ㄹ' and b == 'ㄱ':
		return 'ㄺ'
	elif a == 'ㄹ' and b == 'ㅁ':
		return 'ㄻ'
	elif a == 'ㄹ' and b == 'ㅂ':
		return 'ㄼ'
	elif a == 'ㄹ' and b == 'ㅅ':
		return 'ㄽ'
	elif a == 'ㄹ' and b == 'ㅌ':
		return 'ㄾ'
	elif a == 'ㄹ' and b == 'ㅍ':
		return 'ㄿ'
	elif a == 'ㄹ' and b == 'ㅎ':
		return 'ㅀ'
	elif a == 'ㅂ' and b == 'ㅅ':
		return 'ㅄ'									# 단일문자들을 이중문자로 합침
			

def Combine2Words(lst):											# 튜플안의 단일문자들을 이중문자로
	i = 0
	Two_list = []
	while i != len(D_list):
		if type(lst[i]) == tuple:								# 해당자료의 자료형이 튜플이라면(분리된 이중문자)
			Two_list.append(Word2DoubleWord(lst[i][0], lst[i][1]))	# 이중문자로 만들어 Two_list에 추가
		else:													# 튜플이 아니라면 (단일문자)
			Two_list.append(lst[i])								# 바로 Two_list에 추가
		i += 1													# 다음 인덱스로 이동

	return Two_list




# ---------------------- 테스트 코드 ----------------------------------------------

morseCodeTree = make_morse_tree()								# 모스 코드의 결정트리 생성
str = input("입력 문장 : ")
print("조합형 : ", end = '')
print("".join(Complete2Combination(str)))						# 반환받은 조합형 리스트를 문자열로 출력

E_list = []														# 출력용 인코딩 리스트 (튜플 제거)
E2_list = []													# 인코딩 리스트
D_list = []														# 디코딩 리스트

for ch in Complete2Combination(str):
	code = encode(ch)											# 문자를 인코딩하여 code에 저장
	E2_list.append(code)										# 코드를 E2_list에 추가 (튜플 포함)
	if type(code) == tuple:										# 자료형이 튜플이면
		for i in code:
			E_list.append(i)									# 튜플제거하여 E_list에 추가
	else:														# 튜플이 아니면
		E_list.append(code)										# 바로 E_list에 추가

print("Morse Code : ", E_list)									# E_list 출력

print("Decoding : ", end = '')									
for code in E_list:
	ch = decode(morseCodeTree, code)							# E_list의 코드들을 디코딩하여 출력
	print(ch, end = '')

for code in E2_list:										
	if type(code) == tuple:										# E2_list 자료의 자료형이 튜플이면
		ch = decode(morseCodeTree, code[0])						# 튜플안 코드들을 디코딩하여
		ch1 = decode(morseCodeTree, code[1])					# 각각 ch, ch1에 저장하고
		D_list.append((ch, ch1))								# D_list에 튜플로 추가
	else:														# 튜플이 아니라면
		ch2 = decode(morseCodeTree, code)
		D_list.append(ch2)										# 디코딩하여 D_list에 추가


D2_list = Combine2Words(D_list)									# D_list의 튜플안 문자들을 이중문자로 만듦
print("\n완성형 : ", ''.join(Combination2Complete(D2_list)))	# D2_list의 문자들을 완성형으로 만들고 문자열로 출력

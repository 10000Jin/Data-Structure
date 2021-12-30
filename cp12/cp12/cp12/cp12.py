
#P12.1

def check_bubble_sort(A):
	n = len(A)
	bChanged = False
	for i in range(n-1):
		if A[i] > A[i+1]:
			bChanged = True

	result = not bChanged
	return result



A = [3, 6, 4, 1, 9, 0, 3]
B = [1, 2, 5, 6, 7, 9] 

print("A = ", A)
print("정렬되어 있는가? ", check_bubble_sort(A))
print()
print("B = ", B)
print("정렬되어 있는가? ", check_bubble_sort(B))
print()

C = []
C = input("배열을 입력하시오 : C = ").split(" ")
print("정렬되어 있는가? ", check_bubble_sort(C))
print()
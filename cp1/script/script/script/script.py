def move(m, i, j):
    num = 0
    if i == 0:
        if j == 0:
            num += (m[i+1][j] + m[i][j+1])
        elif j == 1:
            num += (m[i][j-1] + m[i+1][j] + m[i][j+1])
        elif j == 2:
            num += (m[i][j-1] + m[i+1][j])
    if i == 1:
        if j == 0:
            num += (m[i-1][j] + m[i+1][j] + m[i][j+1])
        elif j == 1:
            num += (m[i][j-1] + m[i+1][j] + m[i][j+1] + m[i-1][j])
        elif j == 2:
            num += (m[i][j-1] + m[i-1][j] + m[i+1][j])
    if i == 2:
        if j == 0:
            num += (m[i-1][j] + m[i][j+1])
        elif j == 1:
            num += (m[i][j-1] + m[i][j+1] + m[i-1][j])
        elif j == 2:
            num += (m[i][j-1] + m[i-1][j])
    return num
    


map = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
new_map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
whole = 0

for x in range(18):
    ex_map = map
    for i in range(3):
        for j in range(3):
            new_map[i][j] = move(ex_map, i, j)

    map = new_map
    if x != 17:
        new_map = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
      

for x in new_map:
    for y in x:
        whole += y

print("전체 경우의 수 :",whole)
print("Hospital에 있을 경우의 수 :",new_map[0][0])
print('Hospital에 있을 확률 : {:.2f}%'.format(new_map[0][0] / whole))
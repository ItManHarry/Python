#数字游戏
SIZE = 5
v_array = []
for i in range(SIZE):
    v_array.append([0] * SIZE)
print(v_array)
for i in range(SIZE):
    for j in range(SIZE):
        print(v_array[i][j], end='')

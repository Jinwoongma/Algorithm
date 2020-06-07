def move_cube(dir, arr):
    if dir == 4:
        arr[1], arr[2], arr[3], arr[0], arr[4], arr[5] = arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]
    elif dir == 3:
        arr[3], arr[0], arr[1], arr[2], arr[4], arr[5] = arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]
    elif dir == 1:
        arr[0], arr[5], arr[2], arr[4], arr[1], arr[3] = arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]
    elif dir == 2:
        arr[0], arr[4], arr[2], arr[5], arr[3], arr[1] = arr[0], arr[1], arr[2], arr[3], arr[4], arr[5]
    return arr

def move_map(dir, x, y, y_end, x_end, ismove):
    if dir == 4:
        if y + 1 >= y_end:
            x, y, = x, y
            ismove = False
        else:
            x, y = x, y+1
            ismove = True
    elif dir == 3:
        if y - 1 < 0:
            x, y = x, y
            ismove = False
        else:
            x, y = x, y-1
            ismove = True
    elif dir == 2:
        if x - 1 < 0:
            x, y = x, y
            ismove = False
        else:
            x, y = x-1, y
            ismove = True
    elif dir == 1:
        if x + 1 >= x_end:
            x, y, = x, y
            ismove = False
        else:
            x, y = x+1, y
            ismove = True
    return x, y, ismove


N, M, x, y, K = map(int, input().split())
maps = []

for i in range(N):
    temp = list(map(int, input().split()))
    maps.append(temp)
dir_list = list(map(int, input().split()))

#print(maps)
#print(y, x)
cube = [2, 1, 5, 6, 4, 3]
number = [0] * 7
for i in range(len(dir_list)):

    x, y, ismove = move_map(dir_list[i], x, y, N, M, 1)
    #print(y, x, ismove)
    #print(cube)
    if ismove == True:
        cube = move_cube(dir_list[i], cube)
        # 이동한 지도가 0이라면 -> 주사위의 바닥면에 쓰여 있는 수가 칸에 복사된다
        if maps[y][x] == 0:
            maps[y][x] = number[cube[3]]
        # 이동한 지도가 0이면 -> 큐브 아랫면에 지도 복사, 큐브아래 = 0
        else:
            number[cube[3]] = maps[y][x]
            maps[y][x] = 0

        print(number[cube[1]])
    else:
        continue







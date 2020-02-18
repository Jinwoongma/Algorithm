def search(y, x):
    count = 0
    loc = []
    for dir in range(4):
        ty, tx = y + up_dy[dir], x + up_dx[dir]
        if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
        if MAP[ty][tx] != -1:
            count += 1
            loc.append([ty, tx])
    return count, loc

r, c, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(r)]
up_dy = [0, -1, 0, 1]; up_dx = [1, 0, -1, 0]
down_dy = [0, 1, 0, -1]; down_dx = [1, 0, -1, 0]

cleaner = []
for i in range(r):
    if MAP[i][0] == -1:
        cleaner.append(i)

for t in range(T):
    temp = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            count, loc = 0, []
            if MAP[i][j] != 0 and MAP[i][j] != -1:
                count, loc = search(i, j)
                # print(count, loc)
            temp[i][j] -= (MAP[i][j] // 5) * count
            for k in range(len(loc)):
                temp[loc[k][0]][loc[k][1]] += MAP[i][j] // 5

    for i in range(r):
        for j in range(c):
            MAP[i][j] += temp[i][j]

    y, x, dir= cleaner[0], 1, 0
    temp = 0
    while True:
        ty, tx = y + up_dy[dir], x + up_dx[dir]
        if ty < 0 or ty >= r or tx < 0 or tx >= c:
            dir += 1
            continue
        if MAP[ty][tx] == -1:
            MAP[y][x] = temp
            break
        else:
            MAP[y][x], temp = temp, MAP[y][x]
            y, x = ty, tx

    y, x, dir = cleaner[1], 1, 0
    temp = 0
    while True:
        ty, tx = y + down_dy[dir], x + down_dx[dir]
        if ty < 0 or ty >= r or tx < 0 or tx >= c:
            dir += 1
            continue
        if MAP[ty][tx] == -1:
            MAP[y][x] = temp
            break
        else:
            MAP[y][x], temp = temp, MAP[y][x]
            y, x = ty, tx

count = 0
for i in range(r):
    for j in range(c):
        if MAP[i][j] == -1: continue
        count += MAP[i][j]
print(count)

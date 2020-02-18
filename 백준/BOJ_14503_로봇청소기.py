def turnLeft(dir):
    if dir == 0: return 3
    elif dir == 1: return 0
    elif dir == 2: return 1
    else: return 2

N, M = map(int, input().split())
y, x, dir = map(int, input().split())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
MAP = [list(map(int, input().split())) for _ in range(N)]
MAP[y][x] = -1
count = 1

while True:
    for i in range(4):
        dir = turnLeft(dir)
        ty, tx = y + dy[dir], x + dx[dir]
        if MAP[ty][tx] == 0:
            count += 1
            MAP[ty][tx] = -1
            y, x = ty, tx
            break
    else:
        ty, tx = y - dy[dir], x - dx[dir]
        if MAP[ty][tx] == 1:
            break
        else:
            y, x = ty, tx

print(count)
# for i in range(M):
#     print(MAP[i])
# print()

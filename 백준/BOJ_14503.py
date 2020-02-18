row, col = map(int, input().split())
y, x, dir = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(row)]
dx = [0, 1, 0, -1]  # 북 동 남 서
dy = [-1, 0, 1, 0]

def left_dir(dir):
    if dir == 0: return 3
    elif dir == 1: return 0
    elif dir == 2: return 1
    else: return 2

def dfs(y, x, dir):
    global count
    if data[y][x] == 1:
        return
    if data[y][x] == 0:
        data[y][x] = 2
        count += 1

    for i in range(4):
        dir = left_dir(dir)
        ty, tx = y + dy[dir], x + dx[dir]
        if data[ty][tx] == 0:
            dfs(ty, tx, dir)
            return

    ty, tx = y - dy[dir], x - dx[dir]
    dfs(ty, tx, dir)

count = 0
dfs(y, x, dir)
print(count)
# for i in range(row):
#     print(data[i])
# print()

def check():
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if len(MAP[r][c]) >= 4:
                return True
    return False

N, K = map(int, input().split())
board = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
MAP = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
dy = [0, 0, 0, -1, 1]; dx = [0, 1, -1, 0, 0]
move = []
for i in range(K):
    y, x, d = map(int, input().split())
    MAP[y][x].append(i+1)
    move.append([y, x, d])
flag2 = False
turn = 0

while True:
    if turn > 1000:
        print(-1)
        break

    for i in range(K):
        y, x, d = move[i]
        ty, tx = y + dy[d], x + dx[d]

        if ty < 1 or ty > N or tx < 1 or tx > N or board[ty][tx] == 2:
            if d == 1: d = 2
            elif d == 2: d = 1
            elif d == 3: d = 4
            elif d == 4: d = 3
            move[i][2] = d
            ty, tx = y + dy[d], x + dx[d]
            if check():
                flag2 = True
                break

        if ty < 1 or ty > N or tx < 1 or tx > N or board[ty][tx] == 2:
            if check():
                flag2 = True
                break

        elif board[ty][tx] == 0:
            flag = False
            temp = []
            for j in range(len(MAP[y][x])):
                if MAP[y][x][j] == i + 1:
                    flag = True
                if flag:
                    move[MAP[y][x][j] - 1][0], move[MAP[y][x][j] - 1][1] = ty, tx
                    MAP[ty][tx].append(MAP[y][x][j])
                else:
                    temp.append(MAP[y][x][j])
            MAP[y][x] = temp
            if check():
                flag2 = True
                break

        elif board[ty][tx] == 1:
            flag = False
            for j in range(len(MAP[y][x]) - 1, -1, -1):
                if MAP[y][x][j] == i + 1:
                    flag = True
                    move[MAP[y][x][j] - 1][0], move[MAP[y][x][j] - 1][1] = ty, tx
                    MAP[ty][tx].append(MAP[y][x][j])
                    MAP[y][x].pop(j)
                if not flag:
                    move[MAP[y][x][j] - 1][0], move[MAP[y][x][j] - 1][1] = ty, tx
                    MAP[ty][tx].append(MAP[y][x][j])
                    MAP[y][x].pop(j)
            if check():
                flag2 = True
                break

    if flag2:
        print(turn + 1)
        break
    else:
        turn += 1


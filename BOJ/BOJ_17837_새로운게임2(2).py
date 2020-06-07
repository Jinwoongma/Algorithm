# 20_04_26 15:10 ~

def ChangeDir(d):
    if d == 0: return 1
    elif d == 1: return 0
    elif d == 2: return 3
    elif d == 3: return 2


N, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dy = [0, 0, -1, 1]; dx = [1, -1, 0, 0]
current = [[[] for _ in range(N)] for _ in range(N)]
visited = [[set() for _ in range(N)] for _ in range(N)]
chess = []
for i in range(K):
    y, x, d = map(int, input().split())
    chess.append([y - 1, x - 1, d - 1])
    current[y - 1][x - 1].append([i, d - 1])

turn = 0
flag = False
while not flag:
    if turn > 1000:
        answer = -1
        break

    for i in range(K):
        y, x, d = chess[i]
        ny, nx = y + dy[d], x + dx[d]
        for j in range(len(current[y][x])):
            if current[y][x][j][0] == i:
                index = j
        temp = current[y][x][index:]  # 이동될 말 정보들

        # for r in range(N):
        #     print(current[r])
        # print()

        if ny < 0 or ny >= N or nx < 0 or nx >= N or MAP[ny][nx] == 2:
            nny, nnx, nnd = y - dy[d], x - dx[d], ChangeDir(d)
            if 0 <= nny < N and 0 <= nnx < N and MAP[nny][nnx] != 2:
                temp[0][1] = nnd
                if MAP[nny][nnx] == 0:
                    current[y][x], current[nny][nnx] = current[y][x][:index], current[nny][nnx] + temp
                    chess[i][0], chess[i][1], chess[i][2] = nny, nnx, nnd
                    for k in range(len(temp)):
                        chess[temp[k][0]][0], chess[temp[k][0]][1] = nny, nnx

                elif MAP[nny][nnx] == 1:
                    temp.reverse()
                    current[y][x], current[nny][nnx] = current[y][x][:index], current[nny][nnx] + temp
                    chess[i][0], chess[i][1], chess[i][2] = nny, nnx, nnd
                    for k in range(len(temp)):
                        chess[temp[k][0]][0], chess[temp[k][0]][1] = nny, nnx

        elif MAP[ny][nx] == 0:
            current[y][x], current[ny][nx] = current[y][x][:index], current[ny][nx] + temp
            chess[i][0], chess[i][1] = ny, nx
            for k in range(len(temp)):
                chess[temp[k][0]][0], chess[temp[k][0]][1] = ny, nx

        elif MAP[ny][nx] == 1:
            temp.reverse()
            current[y][x], current[ny][nx] = current[y][x][:index], current[ny][nx] + temp
            chess[i][0], chess[i][1] = ny, nx
            for k in range(len(temp)):
                chess[temp[k][0]][0], chess[temp[k][0]][1] = ny, nx

        for r in range(N):
            for c in range(N):
                if len(current[r][c]) >= 4:
                    flag = True

    if flag:
        answer = turn + 1
        break
    else:
        turn += 1

print(answer)
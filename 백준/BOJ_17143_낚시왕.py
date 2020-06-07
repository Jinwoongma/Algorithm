R, C, N = map(int, input().split())
MAP = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
dy = [0, -1, 1, 0, 0]
dx = [0, 0, 0, 1, -1]
for i in range(N):
    r, c, s, d, z = map(int, input().split())
    MAP[r][c] = [s, d, z]

catch = 0
for c in range(1, C + 1):
    # 상어 잡기
    for r in range(1, R + 1):
        if MAP[r][c] != 0:
            catch += MAP[r][c][2]
            MAP[r][c] = 0
            break

    # # 상어 이동
    temp = [[0 for _ in range(C + 1)] for _ in range(R + 1)]
    for i in range(1, R + 1):
        for j in range(1, C + 1):
            if MAP[i][j] != 0:
                s, d = MAP[i][j][0], MAP[i][j][1]
                if d == 1 or d == 2:
                    s = s % ((R - 1) * 2)
                elif d ==3 or d == 4:
                    s = s % ((C - 1) * 2)
                ty, tx = i, j
                for k in range(s):
                    ty += dy[d]
                    tx += dx[d]
                    if ty < 1 or ty > R or tx < 1 or tx > C:
                        if d == 1: d = 2
                        elif d == 2: d = 1
                        elif d == 3: d = 4
                        elif d == 4: d = 3
                        MAP[i][j][1] = d
                        ty += (dy[d] * 2)
                        tx += (dx[d] * 2)
                        continue
                if temp[ty][tx] != 0:
                    if temp[ty][tx][2] < MAP[i][j][2]:
                        temp[ty][tx] = MAP[i][j]
                else:
                    temp[ty][tx] = MAP[i][j]
    MAP = temp

print(catch)
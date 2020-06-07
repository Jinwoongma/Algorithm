R, C, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
dust = []
cleaner = []
for i in range(R):
    for j in range(C):
        if MAP[i][j] > 0:
            dust.append((i, j))
        elif MAP[i][j] == -1:
            cleaner.append((i, j))

while T:
    new_MAP = [[[] for _ in range(C)] for _ in range(R)]

    # 먼지 확산
    for y, x in dust:
        cnt = 0
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
            if MAP[ty][tx] == -1:
                continue
            cnt += 1
            new_MAP[ty][tx].append(MAP[y][x] // 5)
        new_MAP[y][x].append(MAP[y][x] - (cnt * (MAP[y][x] // 5)))
    for y, x in cleaner:  # 공기청정기 위치
        new_MAP[y][x].append(-1)
    for i in range(R):  # 더해주기
        for j in range(C):
            MAP[i][j] = sum(new_MAP[i][j])

    # 윗방향 이동
    y, x, d = cleaner[0][0], cleaner[0][1], 3
    temp = 0
    while True:
        ty, tx = y + dy[d], x + dx[d]
        if d == 3 and tx >= C:
            d = 0
            ty, tx = y + dy[d], x + dx[d]
        elif d == 0 and ty < 0:
            d = 2
            ty, tx = y + dy[d], x + dx[d]
        elif d == 2 and tx < 0:
            d = 1
            ty, tx = y + dy[d], x + dx[d]

        if not MAP[ty][tx] == -1:
            MAP[ty][tx], temp = temp, MAP[ty][tx]
            y, x = ty, tx
        else:
            break

    # 아랫방향 이동
    y, x, d = cleaner[1][0], cleaner[1][1], 3
    temp = 0
    while True:
        ty, tx = y + dy[d], x + dx[d]
        if d == 3 and tx >= C:
            d = 1
            ty, tx = y + dy[d], x + dx[d]
        elif d == 1 and ty >= R:
            d = 2
            ty, tx = y + dy[d], x + dx[d]
        elif d == 2 and tx < 0:
            d = 0
            ty, tx = y + dy[d], x + dx[d]

        if not MAP[ty][tx] == -1:
            MAP[ty][tx], temp = temp, MAP[ty][tx]
            y, x = ty, tx
        else:
            break

    # 먼지 세기
    ans = 0
    dust = []
    for i in range(R):
        for j in range(C):
            if MAP[i][j] > 0:
                dust.append((i, j))
                ans += MAP[i][j]
    T -= 1

print(ans)
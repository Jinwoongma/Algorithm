# 0140 - 0226

def solve(sy, sx, sd):
    score = 0
    y, x, d = sy + dy[sd], sx + dx[sd], sd
    while True:
        if y < 0 or y >= N or x < 0 or x >= N:
            if d == 0: d = 1
            elif d == 1: d = 0
            elif d == 2: d = 3
            elif d == 3: d = 2
            score += 1
            y, x = y + dy[d], x + dx[d]
        if MAP[y][x] == -1 or (y == sy and x == sx):
            break
        elif 1 <= MAP[y][x] <= 5:
            if MAP[y][x] == 1:
                if d == 0: d = 1
                elif d == 1: d = 3
                elif d == 2: d = 0
                elif d == 3: d = 2
            elif MAP[y][x] == 2:
                if d == 0: d = 3
                elif d == 1: d = 0
                elif d == 2: d = 1
                elif d == 3: d = 2
            elif MAP[y][x] == 3:
                if d == 0: d = 2
                elif d == 1: d = 0
                elif d == 2: d = 3
                elif d == 3: d = 1
            elif MAP[y][x] == 4:
                if d == 0: d = 1
                elif d == 1: d = 2
                elif d == 2: d = 3
                elif d == 3: d = 0
            if MAP[y][x] == 5:
                if d == 0: d = 1
                elif d == 1: d = 0
                elif d == 2: d = 3
                elif d == 3: d = 2
            score += 1
            y += dy[d]; x += dx[d]

        elif 6 <= MAP[y][x] <= 10:
            first, second = warm[MAP[y][x]]
            if (y, x) == first:
                y, x = second[0], second[1]
            else:
                y, x = first[0], first[1]
            y += dy[d]; x += dx[d]

        elif MAP[y][x] == 0:
            y += dy[d]; x += dx[d]
    return score


TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]  # 상 하 좌 우
    warm = [[] for _ in range(11)]
    ans = -1
    for i in range(N):
        for j in range(N):
            if 6 <= MAP[i][j] <= 10:
                warm[MAP[i][j]].append((i, j))

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 0:
                for dir in range(4):
                    ans = max(ans, solve(i, j, dir))

    print('#{} {}'.format(tc + 1, ans))


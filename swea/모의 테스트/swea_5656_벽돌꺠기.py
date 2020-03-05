from _collections import deque

def copyMap(depth):
    for i in range(r):
        for j in range(c):
            MAP[depth][i][j] = MAP[depth - 1][i][j]


def bricGame(depth, y, x):
    rep = MAP[depth][y][x]
    MAP[depth][y][x] = 0
    ans = 1
    for p in range(rep):
        for dir in range(4):
            ty, tx = y + (dy[dir] * p), x + (dx[dir] * p)
            if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
            if MAP[depth][ty][tx] != 0:
                ans += bricGame(depth, ty, tx)
    return ans


def change(depth):
    Q = deque()
    for i in range(c):
        for j in range(r - 1, -1, -1):
            if MAP[depth][j][i]:
                Q.append(MAP[depth][j][i])
                MAP[depth][j][i] = 0
        j = r - 1
        while Q:
            MAP[depth][j][i] = Q.popleft()
            j -= 1


def solve(depth):
    if depth > N:
        return 0
    ans = 0
    # 벽돌 깨기
    for i in range(c):
        copyMap(depth)
        temp = 0
        flag = True
        for j in range(r):
            if MAP[depth][j][i] != 0:
                flag = False
                temp = bricGame(depth, j, i)
                break
        if flag: continue

        change(depth)
        ans = max(ans, solve(depth + 1) + temp)

    return ans


TC = int(input())
for tc in range(TC):
    N, c, r = map(int, input().split())
    MAP = [[[0 for _ in range(c)] for _ in range(r)] for _ in range(5)]
    SUM = 0
    for i in range(r):
        temp = list(map(int, input().split()))
        MAP[0][i] = temp
        for j in range(c):
            if MAP[0][i][j] != 0:
                SUM += 1

    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    print('#{} {}'.format(tc + 1, SUM - solve(1)))
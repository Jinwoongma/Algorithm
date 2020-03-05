from _collections import deque
import sys
sys.stdin = open('input.txt', 'r')

def copyMAP(depth):
    for i in range(H):
        for j in range(W):
            MAP[depth][i][j] = MAP[depth - 1][i][j]


def solve(depth):
    if depth > N:
        return 0
    ans = 0
    for i in range(W):
        copyMAP(depth)
        flag = True
        temp = 0
        for j in range(H):
            if MAP[depth][j][i]:
                flag = False
                temp = dfs(depth, j, i)
                break
        if flag: continue
        pulldown(depth)
        ans = max(ans, temp + solve(depth + 1))
    return ans


def dfs(depth, y, x):
    rep = MAP[depth][y][x]
    MAP[depth][y][x] = 0
    break_num = 1
    for i in range(rep):
        for j in range(4):
            ty, tx = y + (dy[j] * i), x + (dx[j] * i)
            if ty < 0 or ty >= H or tx < 0 or tx >= W: continue
            if MAP[depth][ty][tx] != 0:
                break_num += dfs(depth, ty, tx)
    return break_num


def pulldown(depth):
    q = deque()
    for i in range(W):
        for j in range(H - 1, -1, -1):
            if MAP[depth][j][i]:
                q.append(MAP[depth][j][i])
            MAP[depth][j][i] = 0

        for j in range(H-1, H - 1 - len(q), -1):
            MAP[depth][j][i] = q.popleft()


TC = int(input())
for tc in range(TC):
    N, W, H = map(int, input().split())
    MAP = [[[0 for _ in range(W)] for _ in range(H)] for _ in range(5)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    SUM = 0
    for i in range(H):
        MAP[0][i] = list(map(int, input().split()))
        for j in range(W):
            if MAP[0][i][j]:
                SUM += 1

    max_break = solve(1)

    print(SUM - max_break)
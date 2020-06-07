import sys
sys.stdin = open('input_1226.txt', 'r')

def dfs(y, x):
    visited[y][x] = True
    if MAP[y][x] == '3':
        return 1
    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= 16 or tx < 0 or tx >= 16: continue
        if visited[ty][tx]: continue
        if MAP[ty][tx] == '0' or MAP[ty][tx] == '3':
            if dfs(ty, tx): return 1
    return 0

for tc in range(1, 11):
    t = int(input())
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    MAP = [str(input()) for _ in range(16)]
    visited = [[False for _ in range(16)] for _ in range(16)]

    ans = 0
    for i in range(16):
        for j in range(16):
            if MAP[i][j] == '2':
                s_y, s_x = i, j

    print(dfs(s_y, s_x))
    # print('#{} {}'.format(tc, ans))
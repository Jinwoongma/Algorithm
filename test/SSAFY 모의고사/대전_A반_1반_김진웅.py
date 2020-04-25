# import sys
# sys.stdin = open('input.txt', 'r')

def dfs(y, x):
    visited[y][x] = True
    for dir in range(8):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= 10 or tx < 0 or tx >= 10: continue
        if not visited[ty][tx] and MAP[ty][tx] == 1:
            dfs(ty, tx)


TC = int(input())
for tc in range(TC):
    MAP = [list(map(int, input().split())) for _ in range(10)]
    visited = [[False for _ in range(10)] for _ in range(10)]
    dy = [1, 1, 1, 0, -1, -1, -1, 0]; dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    answer = 0
    for i in range(10):
        for j in range(10):
            if not visited[i][j] and MAP[i][j] == 1:
                answer += 1
                dfs(i, j)
    print('#{} {}'.format(tc + 1, answer))
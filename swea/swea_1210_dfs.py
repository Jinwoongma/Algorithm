import sys
sys.stdin = open('input_1210.txt', 'r')

def dfs(y, x):
    if y == 0 and not len(result) != 0:
        result.append(x)
    visited[y][x] = True
    for dir in range(3):
        ty, tx = y + dy[dir], x + dx[dir]
        if 0 <= ty < 100 and 0 <= tx < 100:
            if MAP[ty][tx] == 1 and not visited[ty][tx]:
                dfs(ty, tx)

for tc in range(1, 11):
    t = int(input())
    dy = [0, 0, -1]
    dx = [1, -1, 0]  # 우 -> 좌 -> 하
    MAP = [list(map(int, input().split())) for _ in range(100)]
    visited = [[False for _ in range(100)] for _ in range(100)]
    for i in range(100):
        if MAP[99][i] == 2:
            x = i
    result = []
    dfs(99, x)
    print('#{} {}'.format(tc + 1, result[0]))
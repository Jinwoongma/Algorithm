import sys
sys.stdin = open('input.txt', 'r')


def dfs(y, x, length, cut):
    global max_length
    max_length = max(max_length, length)

    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
        if not cut:
            if MAP[y][x] > MAP[ty][tx]:
                if not visited[ty][tx]:
                    visited[ty][tx] = True
                    dfs(ty, tx, length + 1, 0)
                    visited[ty][tx] = False
            else:
                if (MAP[ty][tx] - MAP[y][x] + 1) <= K:
                    if not visited[ty][tx]:
                        temp = MAP[ty][tx]
                        MAP[ty][tx] = MAP[y][x] - 1
                        visited[ty][tx] = True
                        dfs(ty, tx, length + 1, 1)
                        visited[ty][tx] = False
                        MAP[ty][tx] = temp
        if cut:
            if MAP[y][x] > MAP[ty][tx]:
                if not visited[ty][tx]:
                    visited[ty][tx] = True
                    dfs(ty, tx, length + 1, 1)
                    visited[ty][tx] = False


TC = int(input())
for tc in range(TC):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    max_length = -1
    max_h, max_idx = -1, []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] > max_h:
                max_h = MAP[i][j]
                max_idx = [[i, j]]
            elif MAP[i][j] == max_h:
                max_idx.append([i, j])

    for i in range(len(max_idx)):
        visited = [[0 for _ in range(N)] for _ in range(N)]
        y, x = max_idx[i]
        visited[y][x] = True
        dfs(y, x, 1, 0)
    print('#{} {}'.format(tc + 1, max_length))

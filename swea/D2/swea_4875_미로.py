# 0: 통로,  1: 벽,  2: 출발,  3: 도착
def dfs(y, x):
    global flag
    if MAP[y][x] == '3':
        flag = True
        return
    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
        if visited[ty][tx]: continue
        if MAP[ty][tx] == '0' or MAP[ty][tx] == '3':
            visited[ty][tx] = True
            dfs(ty, tx)
            visited[ty][tx] = False


TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [str(input()) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    dy = [0, 0, -1, 1];
    dx = [-1, 1, 0, 0]  # 좌, 우, 상
    flag = False

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == '2':
                y, x = i, j

    dfs(y, x)
    if flag:
        print('#{} {}'.format(tc + 1, 1))
    else:
        print('#{} {}'.format(tc + 1, 0))
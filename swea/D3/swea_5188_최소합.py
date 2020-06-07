from _collections import deque

TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    D = [[0xfffff for _ in range(N)] for _ in range(N)]
    dy = [0, 1]; dx = [1, 0]
    D[0][0] = MAP[0][0]
    Q = deque()
    Q.append([0, 0])
    while Q:
        y, x = Q.popleft()
        for dir in range(2):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
            if D[ty][tx] > D[y][x] + MAP[ty][tx]:
                D[ty][tx] = D[y][x] + MAP[ty][tx]
                Q.append([ty, tx])

    print('#{} {}'.format(tc + 1, D[N - 1][N - 1]))
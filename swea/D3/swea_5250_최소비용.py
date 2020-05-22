from _collections import deque

TC = int(input())
for tc in range(TC):
    N = int(input())
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    MAP = [list(map(int, input().split())) for _ in range(N)]
    D = [[0xfffff for _ in range(N)] for _ in range(N)]
    D[0][0] = 0
    Q = deque()
    Q.append([0, 0])
    while Q:
        y, x = Q.popleft()
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= N or tx < 0 or tx >= N:
                continue
            cur_height, next_height = MAP[y][x], MAP[ty][tx]
            if cur_height < next_height:
                plus = (next_height - cur_height) + 1
            else: plus = 1

            if D[ty][tx] > D[y][x] + plus:
                D[ty][tx] = D[y][x] + plus
                Q.append([ty, tx])

    print('#{} {}'.format(tc + 1, D[N - 1][N - 1]))

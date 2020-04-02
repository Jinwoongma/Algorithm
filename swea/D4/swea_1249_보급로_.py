from _collections import deque
TC = int(input())
for tc in range(TC):
    N = int(input())
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    MAP = [list(map(int, input().strip())) for _ in range(N)]
    dp = [[-1 for _ in range(N)] for _ in range(N)]

    Q = deque()
    Q.append([0, 0])
    dp[0][0] = 0

    while Q:
        y, x = Q.popleft()
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
            if dp[ty][tx] == -1:
                dp[ty][tx] = dp[y][x] + MAP[ty][tx]
                Q.append([ty, tx])
            else:
                if ty == 0 and tx == 0: continue
                if dp[ty][tx] > dp[y][x] + MAP[ty][tx]:
                    dp[ty][tx] = dp[y][x] + MAP[ty][tx]
                    Q.append([ty, tx])
    print('#{} {}'.format(tc + 1, dp[N - 1][N - 1]))
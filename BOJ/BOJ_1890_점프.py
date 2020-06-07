def solve(y, x):
    if y == N - 1 and x == N - 1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    rignt_y, right_x = y, x + MAP[y][x]
    down_y, down_x = y + MAP[y][x], x
    if right_x < N:
        dp[y][x] += solve(rignt_y, right_x)

    if down_y < N:
        dp[y][x] += solve(down_y, down_x)

    return dp[y][x]

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(N)] for _ in range(N)]
print(solve(0, 0))
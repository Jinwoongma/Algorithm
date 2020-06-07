N = int(input())
data = [[0] * N] + [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(3)] for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + data[i][0]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + data[i][1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + data[i][2]

result = min(dp[N])

print(result)

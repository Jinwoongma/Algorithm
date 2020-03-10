N = int(input())

dp = [[0 for _ in range(10)] for _ in range(N + 1)]
for i in range(10):
    dp[1][i] = 1

if N >= 2:
    for i in range(2, N + 1):
        for j in range(10):
            for k in range(j, -1, -1):
                dp[i][j] += dp[i - 1][k]

print(sum(dp[-1]) % 10007)
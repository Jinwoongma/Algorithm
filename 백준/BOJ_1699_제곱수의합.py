N = int(input())
dp = [1000000 for _ in range(N + 1)]
dp[0] = 0

for i in range(N + 1):
    for j in range(int(N**0.5) + 1):
        if i + j**2 <= N and dp[i] != -1:
            dp[i + j**2] = min(dp[i + j**2], dp[i] + 1)

print(dp[-1])
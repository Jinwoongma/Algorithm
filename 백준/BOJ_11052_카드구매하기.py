N = int(input())
price = [0] + list(map(int, input().split()))
dp = [-1 for _ in range(N + 1)]
dp[0] = 0

for i in range(N + 1):
    for j in range(N + 1):
        if i + j <= N and dp[i] != -1:
            dp[i + j] = max(dp[i + j], dp[i] + price[j])

print(dp[-1])

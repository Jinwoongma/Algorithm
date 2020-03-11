N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))

dp = [0 for _ in range(K + 1)]
dp[0] = 1

for i in range(N):
    for j in range(coin[i], K + 1):
        if j - coin[i] >= 0:
            dp[j] += dp[j - coin[i]]

print(dp[-1])

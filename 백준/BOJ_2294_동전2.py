def solve(won):
    if dp[won] != 100000:
        # dp[won] = 0
        for i in range(N):
            temp = won + coin[i]
            if temp > K: continue
            dp[temp] = min(dp[temp], dp[won] + 1)
            solve(temp)


N, K = map(int, input().split())
coin = []
for i in range(N):
    coin.append(int(input()))
coin.sort()
dp = [100000 for _ in range(K + 1)]
dp[0] = 0

for i in range(1, K + 1):
    for j in range(N):
        if i - coin[j] >= 0 and dp[i - coin[j]] != 100000:
            dp[i] = min(dp[i], dp[i - coin[j]] + 1)

# print(dp)

if dp[K] == 100000:
    print(-1)
else:
    print(dp[K])
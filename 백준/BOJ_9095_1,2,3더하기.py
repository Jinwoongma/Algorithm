TC = int(input())
for tc in range(TC):
    N = int(input())
    dp = [0 for _ in range(12)]
    dp[1], dp[2], dp[3] = 1, 2, 4

    if N >= 4:
        for i in range(4, N + 1):
            dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]

    print(dp[N])
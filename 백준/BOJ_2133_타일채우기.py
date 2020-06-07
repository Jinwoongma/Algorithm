N = int(input())
dp = [0 for _ in range(40)]
dp[0], dp[1], dp[2] = 1, 0, 3

if N % 2 == 0:
    for i in range(4, N + 1):
        if i % 2 == 0:
            dp[i] = 3 * dp[i - 2]
            if i >= 4:
                sub = 4
                while True:
                    if i - sub < 0: break
                    dp[i] += dp[i - sub] * 2
                    sub += 2

print(dp[N])
def solve(length):
    if length == 1:
        return 1
    if length == 2:
        return 3

    if dp[length] != -1:
        return dp[length]

    dp[length] = solve(length - 1) + (solve(length - 2) * 2)
    return dp[length]


N = int(input())
dp = [-1 for _ in range(N + 1)]
print(solve(N) % 10007)
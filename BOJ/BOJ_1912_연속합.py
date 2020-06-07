def solve(s):
    if dp[s] != -1:
        return dp[s]

    ret = num[s]
    ret = max(ret, num[s] + dp[s + 1])

    dp[s] = ret
    return dp[s]

N = int(input())
num = list(map(int, input().split()))
dp = [-1 for _ in range(N + 1)]
result = -1 * 0xfffff
for start in range(N - 1, -1, -1):
    result = max(result, solve(start))

print(result)
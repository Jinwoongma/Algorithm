def solve(s):
    if dp[s] != -1:
        return dp[s]
    ret = 1
    for i in range(s + 1, N):
        if num[i] > num[s]:
            ret = max(ret, solve(i) + 1)
    dp[s] = ret
    return dp[s]

N = int(input())
num = list(map(int, input().split()))
dp = [-1 for _ in range(N)]
result = -1

for start in range(N):
    result = max(result, solve(start))

print(result)
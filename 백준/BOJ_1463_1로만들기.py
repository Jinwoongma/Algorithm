import sys
sys.setrecursionlimit(1000000)

def solve(num):
    if num == 1:
        return 0

    if dp[num] != -1:
        return dp[num]

    ret = 0xfffff
    if num % 2 == 0 :
        ret = 1 + solve(num // 2)
    if num % 3 == 0:
        ret = min(ret, 1 + solve(num // 3))
    if num % 6 != 0:
        ret = min(ret, 1 + solve(num - 1))
    dp[num] = ret
    return dp[num]

N = int(input())
dp = [-1 for _ in range(N + 1)]
print(solve(N))

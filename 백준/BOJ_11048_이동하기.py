import sys
sys.setrecursionlimit(100000)

def solve(y, x):
    if y < 0 or x < 0:
        return 0

    if dp[y][x] != -1:
        return dp[y][x]

    temp = max(solve(y, x - 1), solve(y - 1, x), solve(y - 1, x - 1))
    dp[y][x] = MAP[y][x] + temp
    return dp[y][x]


R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
dp = [[-1 for _ in range(C)] for _ in range(R)]
print(solve(R - 1, C - 1))
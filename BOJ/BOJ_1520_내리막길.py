import sys
sys.setrecursionlimit(1000000)

def solve(y, x):
    if y == R - 1 and x == C - 1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    dp[y][x] = 0
    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
        if MAP[ty][tx] < MAP[y][x]:
            dp[y][x] += solve(ty, tx)

    return dp[y][x]

R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
dp = [[-1 for _ in range(C)] for _ in range(R)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
print(solve(0, 0))
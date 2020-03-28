def dfs(y, x):
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 1
    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
        if MAP[ty][tx] > MAP[y][x]:
            dp[y][x] = max(dp[y][x], dfs(ty, tx) + 1)
    return dp[y][x]


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
dp = [[-1 for _ in range(N)] for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
ans = -1

for i in range(N):
    for j in range(N):
        ans = max(ans, dfs(i, j))

print(ans)
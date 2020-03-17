def dfs(y, x, d):
    global ans, sy, sx
    if ans: return
    visited[y][x] = True
    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= R or tx < 0 or tx >= C:
            continue
        if MAP[ty][tx] == MAP[sy][sx]:
            if not visited[ty][tx]:
                dfs(ty, tx, d + 1)
            else:
                if d >= 4 and [ty, tx] == [sy, sx]:
                    ans = True
                    return


R, C = map(int, input().split())
MAP = [list(map(str, input().strip())) for _ in range(R)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
ans = False

for i in range(R):
    for j in range(C):
        visited = [[False for _ in range(C)] for _ in range(R)]
        dfs(i, j, 1)
        if ans: break
    if ans: break

if ans: print('Yes')
else: print('No')
def dfs(y, x, cnt):
    global max_path
    max_path = max(max_path, cnt)

    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
        if visited[ord(MAP[ty][tx]) - ord('A')]: continue
        visited[ord(MAP[ty][tx]) - ord('A')] = True
        dfs(ty, tx, cnt + 1)
        visited[ord(MAP[ty][tx]) - ord('A')] = False


r, c = map(int, input().split())
MAP = [list(map(str, input().strip())) for _ in range(r)]
visited = [False for _ in range(26)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
visited[ord(MAP[0][0]) - ord('A')] = True
max_path = -1
dfs(0, 0, 1)
print(max_path)
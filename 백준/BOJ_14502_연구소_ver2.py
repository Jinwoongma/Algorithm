def change(MAP, new):
    new_MAP = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if [i, j] in new: new_MAP[i][j] = 1
            else: new_MAP[i][j] = MAP[i][j]
    return new_MAP


def dfs(y, x, map, visited):
    visited[y][x] = True
    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
        if map[ty][tx] != 1 and not visited[ty][tx]:
            map[ty][tx] = 2
            dfs(ty, tx, map, visited)

def combi(index, start):
    global max_safe

    if index == 3:
        new_MAP = change(MAP, arr)
        visited = [[False for _ in range(c)] for _ in range(r)]

        for i in range(len(birus)):
            dfs(birus[i][0], birus[i][1], new_MAP, visited)
        safe_count = 0
        for j in range(r):
            for k in range(c):
                if new_MAP[j][k] == 0:
                    safe_count += 1
        max_safe = max(max_safe, safe_count)
        return

    for i in range(start, N):
        arr.append(zero[i])
        combi(index + 1, i + 1)
        arr.pop()

r, c = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(r)]
max_safe = -1
dy = [1, -1, 0, 0]; dx = [0, 0, -1, 1]
zero = []
birus = []

for i in range(r):
    for j in range(c):
        if MAP[i][j] == 0:
            zero.append([i, j])
        elif MAP[i][j] == 2:
            birus.append([i, j])

N = len(zero)
arr = []
combi(0, 0)

print(max_safe)
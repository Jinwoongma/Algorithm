import sys
sys.setrecursionlimit(100000)

def dfs(y, x, graph):
    visited[y][x] = True
    for w in graph[y][x]:
        ty, tx = w[0], w[1]
        if not visited[ty][tx]:
            dfs(ty, tx, graph)

N = int(input())
MAP = [input() for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
G1 = [[[] for _ in range(N)] for _ in range(N)]
G2 = [[[] for _ in range(N)] for _ in range(N)]

for y in range(N):
    for x in range(N):
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
            if MAP[y][x] == MAP[ty][tx]:
                G1[y][x].append([ty, tx])

            if MAP[y][x] == MAP[ty][tx]:
                G2[y][x].append([ty, tx])
            else:
                if MAP[y][x] == 'R' and MAP[ty][tx] == 'G':
                    G2[y][x].append([ty, tx])
                elif MAP[y][x] == 'G' and MAP[ty][tx] == 'R':
                    G2[y][x].append([ty, tx])

visited = [[False for _ in range(N)] for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count += 1
            dfs(i, j, G1)
print(count, end=' ')

visited = [[False for _ in range(N)] for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            count += 1
            dfs(i, j, G2)
print(count)
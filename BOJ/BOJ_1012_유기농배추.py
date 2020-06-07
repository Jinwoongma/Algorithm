from collections import deque

def bfs(y, x):
    Q = deque()
    Q.append([y, x])
    while Q:
        s = Q.popleft()
        ty, tx = s[0], s[1]
        for w in G[ty][tx]:
            ty, tx = w[0], w[1]
            if visited[ty][tx]: continue
            visited[ty][tx] = True
            Q.append([ty, tx])


TC = int(input())
for tc in range(TC):
    c, r, K = map(int, input().split())
    MAP = [[0 for _ in range(c)] for _ in range(r)]
    G = [[[] for _ in range(c)] for _ in range(r)]
    visited = [[0 for _ in range(c)] for _ in range(r)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]

    for i in range(K):
        x, y = map(int, input().split())
        MAP[y][x] = 1

    for y in range(r):
        for x in range(c):
            for dir in range(4):
               ty, tx = y + dy[dir], x + dx[dir]
               if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
               if MAP[ty][tx] == 1:
                   G[y][x].append([ty, tx])

    count = 0
    for y in range(r):
        for x in range(c):
            if MAP[y][x] == 1 and not visited[y][x]:
                count += 1
                bfs(y, x)

    print(count)
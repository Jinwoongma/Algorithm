# 2020/02/21
# 20:24 ~ 11: 10
from _collections import deque

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
min_path = 0xffffffff

# def dfs(y, x, num):
#     visited[y][x] = True
#     for dir in range(4):
#         ty, tx = y + dy[dir], x + dx[dir]
#         if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
#         if MAP[ty][tx] == 1 and not visited[ty][tx]:
#             MAP[ty][tx] = num
#             dfs(ty, tx, num)

def bfs1(y, x, num):
    Q = deque()
    Q.append([y, x])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[y][x] = True
    while Q:
        y, x = Q.popleft()
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
            if MAP[ty][tx] == 1 and not visited[ty][tx]:
                MAP[ty][tx] = num
                Q.append([ty, tx])


def bfs2(y, x, start):
    global min_path
    Q = deque()
    Q.append([y, x, 0])
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[y][x] = True

    while Q:
        y, x, path = Q.popleft()
        if MAP[y][x] != 0 and MAP[y][x] != start:
            min_path = min(path, min_path)
            break
        if path > min_path:
            break
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
            if MAP[ty][tx] != start and not visited[ty][tx]:
                visited[ty][tx] = True
                Q.append([ty, tx, path + 1])


count = 1
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 1 and not visited[i][j]:
            count += 1
            MAP[i][j] = count
            bfs1(i, j, count)

for i in range(N):
    for j in range(N):
        if MAP[i][j] != 0:
            for dir in range(4):
                ty, tx = i + dy[dir], j + dx[dir]
                if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
                if MAP[ty][tx] == 0:
                    bfs2(ty, tx, MAP[i][j])

print(min_path)
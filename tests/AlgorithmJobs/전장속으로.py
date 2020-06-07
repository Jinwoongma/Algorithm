from _collections import deque


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 0, 0, 1]; dx = [0, -1, 1, 0]
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 9:
            sy, sx = i, j

turn, level, cnt = 0, 2, 0
while True:
    path = []
    for i in range(N):
        for j in range(N):
            Q = deque()
            if 0 < MAP[i][j] < level:
                Q.append([sy, sx, 0])
                visited = [[False for _ in range(N)] for _ in range(N)]
                visited[sy][sx] = True
                while Q:
                    y, x, t = Q.popleft()
                    if y == i and x == j:
                        path.append([i, j, t])
                        break
                    for dir in range(4):
                        ty, tx = y + dy[dir], x + dx[dir]
                        if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
                        if MAP[ty][tx] <= level and not visited[ty][tx]:
                            Q.append([ty, tx, t + 1])
                            visited[ty][tx] = True
    if len(path) == 0:
        break
    else:
        path.sort(key=lambda x:(x[2], x[0], x[1]))
        turn += path[0][2]
        MAP[sy][sx] = 0
        sy, sx = path[0][0], path[0][1]
        MAP[sy][sx] = 9
        cnt += 1
        if cnt == level:
            level += 1
            cnt = 0
print('{}'.format(turn))
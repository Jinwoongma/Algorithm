from _collections import deque
N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]

for r in range(N):
    for c in range(N):
        if MAP[r][c] == 9:
            my, mx = r, c

size, time, eat = 2, 0, 0

while True:
    path = []
    for r in range(N):
        for c in range(N):
            if 0 < MAP[r][c] < size:
                if r == my and c == mx: continue
                visited = [[False for _ in range(N)] for _ in range(N)]
                Q = deque()
                Q.append([r, c, 0])
                visited[r][c] = True
                while Q:
                    y, x, l = Q.popleft()
                    if y == my and x == mx:
                        path.append([r, c, l])
                        break
                    for dir in range(4):
                        ty, tx = y + dy[dir], x + dx[dir]
                        if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
                        if not visited[ty][tx] and (MAP[ty][tx] == 0 or MAP[ty][tx] == size or MAP[ty][tx] == 9):
                            visited[ty][tx] = True
                            Q.append([ty, tx, l + 1])

    if len(path) == 0:
        print(time)
        break
    else:
        path.sort(key=lambda x: (x[2], x[0], x[1]))
        MAP[my][mx] = 0
        my, mx = path[0][0], path[0][1]
        MAP[my][mx] = 9
        time += path[0][2]
        eat += 1
        if eat == size:
            size += 1
            eat = 0
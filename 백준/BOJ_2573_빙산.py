from _collections import deque
r, c = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(r)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]


def bfs(y, x):
    Q = deque()
    Q.append([y, x])
    visited[y][x] = True
    while Q:
        y, x = Q.popleft()
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
            if not visited[ty][tx] and MAP[ty][tx] != 0:
                Q.append([ty, tx])
                visited[ty][tx] = True


year = 1
while True:
    temp = []
    for i in range(r):
        for j in range(c):
            if MAP[i][j] == 0:
                for dir in range(4):
                    ty, tx = i + dy[dir], j + dx[dir]
                    if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
                    if MAP[ty][tx] > 0: temp.append([ty, tx])

    for i in range(len(temp)):
        if MAP[temp[i][0]][temp[i][1]] > 0:
            MAP[temp[i][0]][temp[i][1]] -= 1

    visited = [[False for _ in range(c)] for _ in range(r)]
    cnt = 0
    for i in range(r):
        for j in range(c):
            if MAP[i][j] != 0 and not visited[i][j]:
                cnt += 1
                bfs(i, j)

    if cnt >= 2:
        print(year)
        break
    elif cnt == 0:
        print(0)
        break
    else:
        year += 1

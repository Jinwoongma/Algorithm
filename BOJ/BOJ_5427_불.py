from _collections import deque

TC = int(input())
for tc in range(TC):
    c, r = map(int, input().split())
    data = [list(input().strip()) for _ in range(r)]
    dist = [[0] * c for _ in range(r)]
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    flag = False
    Q = deque()

    y, x = 0, 0
    for i in range(r):
        for j in range(c):
            if data[i][j] == '*':
                Q.append([i, j, 1])
                dist[i][j] = 1
            elif data[i][j] == '@':
                data[i][j] = '.'
                y, x = i, j

    Q.append([y, x, 0])
    dist[y][x] = 1
    while Q:
        if flag: break
        y, x, f = Q.popleft()

        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= r or tx < 0 or tx >= c:
                if f: continue
                else:
                    print(dist[y][x])
                    flag = True
                    break

            if data[ty][tx] == '#' or dist[ty][tx]: continue
            dist[ty][tx] = dist[y][x] + 1
            Q.append([ty, tx, f])

    if not flag:
        print('IMPOSSIBLE')
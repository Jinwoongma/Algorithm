from _collections import deque

MAP = [list(map(str, input().strip())) for _ in range(8)]
visited = [[[False for _ in range(9)] for _ in range(8)] for _ in range(8)]
dy = [1, 1, 0, -1, 0,  -1, -1, 0, 1]
dx = [0, 1, 1, 1, 0, 0, -1, -1, -1]

flag = False
Q = deque()
Q.append([7, 0, 0])
visited[7][0][0] = True

while Q:
    y, x, cnt = Q.popleft()
    if y == 0 and x == 7:
        flag = True
        break

    for dir in range(9):
        ty, tx = y + dy[dir], x + dx[dir]
        tcnt = min(cnt + 1, 8)
        if ty < 0 or ty >= 8 or tx < 0 or tx >= 8: continue

        if ty - cnt >= 0 and MAP[ty - cnt][tx] == '#':
            continue
        if ty - cnt - 1 >= 0 and MAP[ty - cnt - 1][tx] == '#':
            continue
        if not visited[ty][tx][tcnt]:
            visited[ty][tx][tcnt] = True
            Q.append([ty, tx, tcnt])


if not flag:
    print(0)
else:
    print(1)
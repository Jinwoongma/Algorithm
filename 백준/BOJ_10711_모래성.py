from _collections import deque

r, c = map(int, input().split())
MAP = [list(map(str, input().strip())) for _ in range(r)]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
day = 0

Q = deque()
P = deque()

for i in range(r):
    for j in range(c):
        if MAP[i][j] == '.':
            Q.append([i, j])

while True:
    while Q:
        y, x = Q.popleft()
        for dir in range(8):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
            if MAP[ty][tx] != '.' and MAP[ty][tx] != '9':
                if int(MAP[ty][tx]) - 1 == 0:
                    MAP[ty][tx] = '0'
                    P.append([ty, tx])
                elif int(MAP[ty][tx]) - 1 > 0:
                    MAP[ty][tx] = str(int(MAP[ty][tx]) - 1)

    # for i in range(r):
    #     print(MAP[i])
    # print()

    if not P:
        break
    else:
        Q, P = P, Q
        day += 1

print(day)


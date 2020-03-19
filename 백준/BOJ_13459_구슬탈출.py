from _collections import deque


def move(first, f_color, second, s_color, dir):
    ty, tx = first
    while True:
        if MAP[ty][tx] == '.' and [ty, tx] != second:
            ty, tx = ty + dy[dir], tx + dx[dir]
        if MAP[ty][tx] == 'O':
            flag[f_color] = 1
            first = [-1, -1]
            break
        if MAP[ty][tx] == '#' or [ty, tx] == second:
            break
    if first != [-1, -1]:
        first = [ty - dy[dir], tx - dx[dir]]

    ty, tx = second
    while True:
        if MAP[ty][tx] == '.' and [ty, tx] != first:
            ty, tx = ty + dy[dir], tx + dx[dir]
        if MAP[ty][tx] == 'O':
            flag[s_color] = 1
            second = [-1, -1]
            break
        if MAP[ty][tx] == '#' or [ty, tx] == first:
            break
    if second != [-1, -1]:
        second = [ty - dy[dir], tx - dx[dir]]

    return first, second


R, C = map(int, input().split())
MAP = [list(map(str, input().strip())) for _ in range(R)]
visited = [[[[False for _ in range(C)] for _ in range(R)] for _ in range(C)] for _ in range(R)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
for i in range(R):
    for j in range(C):
        if MAP[i][j] == 'R':
            MAP[i][j] = '.'
            ry, rx = i, j
        if MAP[i][j] == 'B':
            by, bx = i, j
            MAP[i][j] = '.'
        if MAP[i][j] == 'O':
            ey, ex = i, j

Q = deque()
Q.append([[ry, rx], [by, bx], 0])
visited[ry][rx][by][bx] = True
ans = -1

while Q:
    r, b, cnt = Q.popleft()
    if cnt >= 10:
        break
    for dir in range(4):
        flag = [0, 0]
        if dir == 0:
            if r[0] < b[0]: nr, nb = move(r, 1, b, 0, dir)
            else: nb, nr = move(b, 0, r, 1, dir)
        if dir == 1:
            if r[0] > b[0]: nr, nb = move(r, 1, b, 0, dir)
            else: nb, nr = move(b, 0, r, 1, dir)
        if dir == 2:
            if r[1] < b[1]: nr, nb = move(r, 1, b, 0, dir)
            else: nb, nr = move(b, 0, r, 1, dir)
        if dir == 3:
            if r[1] > b[1]: nr, nb = move(r, 1, b, 0, dir)
            else: nb, nr = move(b, 0, r, 1, dir)

        if nr != [-1, -1] and nb != [-1, -1]:
            if visited[nr[0]][nr[1]][nb[0]][nb[1]]:
                continue

        if sum(flag) == 0:
            visited[nr[0]][nr[1]][nb[0]][nb[1]] = True
            Q.append([nr, nb, cnt + 1])
        elif flag[1] == 1 and flag[0] == 0:
            ans = 1
            break
        elif (flag[0] == 1 and flag[1] == 0) or sum(flag) == 2:
            continue
    if ans != -1:
        break

if ans == -1:
    print(0)
else:
    print(1)
from _collections import deque

r, c = map(int, input().split())
MAP = [list(map(str, input().strip())) for _ in range(r)]
visited = [[[[False for _ in range(c)] for _ in range(r)] for _ in range(c)] for _ in range(r)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]

def bfs(ry, rx, by, bx):
    global flag
    Q = deque()
    Q.append([ry, rx, by, bx, 0])
    visited[ry][rx][by][bx] = True

    while Q and not flag:
        ry, rx, by, bx, cnt = Q.popleft()
        # print(ry, rx, by, bx, cnt)
        if cnt > 9:
            print(-1)
            flag = True
            break

        for dir in range(4):
            rflag, bflag = 0, 0
            if dir == 0:  # 위로 기울이기
                if rx != bx:
                    nry, nrx, rflag = move(dir, ry, rx, by, bx)
                    nby, nbx, bflag = move(dir, by, bx, nry, nrx)
                else:
                    if by < ry:
                        nby, nbx, bflag = move(dir, by, bx, ry, rx)
                        nry, nrx, rflag = move(dir, ry, rx, nby, nbx)
                    else:
                        nry, nrx, rflag = move(dir, ry, rx, by, bx)
                        nby, nbx, bflag = move(dir, by, bx, nry, nrx)

            elif dir == 1:  # 아래로 기울이기
                if rx != bx:
                    nry, nrx, rflag = move(dir, ry, rx, by, bx)
                    nby, nbx, bflag = move(dir, by, bx, nry, nrx)
                else:
                    if by < ry:
                        nry, nrx, rflag = move(dir, ry, rx, by, bx)
                        nby, nbx, bflag = move(dir, by, bx, nry, nrx)
                    else:
                        nby, nbx, bflag = move(dir, by, bx, ry, rx)
                        nry, nrx, rflag = move(dir, ry, rx, nby, nbx)

            elif dir == 2:  # 왼쪽으로 기울이기
                if ry != by:
                    nry, nrx, rflag = move(dir, ry, rx, by, bx)
                    nby, nbx, bflag = move(dir, by, bx, nry, nrx)
                else:
                    if rx < bx:
                        nry, nrx, rflag = move(dir, ry, rx, by, bx)
                        nby, nbx, bflag = move(dir, by, bx, nry, nrx)
                    else:
                        nby, nbx, bflag = move(dir, by, bx, ry, rx)
                        nry, nrx, rflag = move(dir, ry, rx, nby, nbx)

            elif dir == 3:  # 오른쪽으로 기울이기
                if ry != by:
                    nry, nrx, rflag = move(dir, ry, rx, by, bx)
                    nby, nbx, bflag = move(dir, by, bx, nry, nrx)
                else:
                    if bx < rx:
                        nry, nrx, rflag = move(dir, ry, rx, by, bx)
                        nby, nbx, bflag = move(dir, by, bx, nry, nrx)
                    else:
                        nby, nbx, bflag = move(dir, by, bx, ry, rx)
                        nry, nrx, rflag = move(dir, ry, rx, nby, nbx)

            if rflag == 1 and bflag == 0:
                print(cnt + 1)
                flag = True
                break
            if rflag == 1 and bflag == 1:
                continue
            if rflag == 0 and bflag == 1:
                continue
            if rflag == 0 and bflag == 0:
                if not visited[nry][nrx][nby][nbx]:
                    visited[nry][nrx][nby][nbx] = True
                    Q.append([nry, nrx, nby, nbx, cnt + 1])


def move(dir, y, x, noty, notx):
    flag = 0
    sy, sx = y, x
    while True:
        ty, tx = sy + dy[dir], sx + dx[dir]
        if MAP[ty][tx] == '#' or (ty == noty and tx == notx):
            break
        elif MAP[ty][tx] == 'O':
            sy, sx = -1, -1
            flag = 1
            break
        else:
            sy, sx = ty, tx
    return sy, sx, flag


for i in range(r):
    for j in range(c):
        if MAP[i][j] == 'R': ry, rx = i, j
        elif MAP[i][j] == 'B': by, bx = i, j

flag = False
bfs(ry, rx, by, bx)
if not flag:
    print(-1)
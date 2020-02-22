from _collections import deque

r, c = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(r)]
visited = [[[False for _ in range(4)] for _ in range(c)] for _ in range(r)]
sy, sx, sdir = map(int, input().split())
ey, ex, edir = map(int, input().split())
dy = [0, 0, 1, -1]; dx = [1, -1, 0, 0]

Q = deque()
Q.append([sy - 1, sx - 1, sdir - 1, 0])
visited[sy - 1][sx - 1][sdir - 1] = True

def turn_left(dir):
    if dir == 0: return 3
    elif dir == 1: return 2
    elif dir == 2: return 0
    else: return 1

def turn_right(dir):
    if dir == 0: return 2
    elif dir == 1: return 3
    elif dir == 2: return 1
    else: return 0

while Q:
    y, x, dir, cnt = Q.popleft()
    # print(y, x, dir, cnt, path)

    if y == ey - 1 and x == ex - 1 and dir == edir - 1:
        print(cnt)
        break

    l_dir, r_dir = turn_left(dir), turn_right(dir)
    if not visited[y][x][l_dir]:
        visited[y][x][l_dir] = True
        Q.append([y, x, l_dir, cnt + 1])
    if not visited[y][x][r_dir]:
        visited[y][x][r_dir] = True
        Q.append([y, x, r_dir, cnt + 1])

    for k in range(1, 4):
        ty, tx = y + (dy[dir] * k), x + (dx[dir] * k)
        if ty < 0 or ty >= r or tx < 0 or tx >= c: break
        if MAP[ty][tx] == 1: break
        if visited[ty][tx][dir]: continue  # 핵심!! 이전 탐색에서 지났던 방향일 경우 break가 아닌 continue!!
        visited[ty][tx][dir] = True
        Q.append([ty, tx, dir, cnt + 1])
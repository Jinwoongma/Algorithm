from _collections import deque


def bfs(y, x, num):
    Q = deque()
    Q.append([y, x])
    check[y][x] = True
    MAP[y][x] = num
    while Q:
        y, x = Q.popleft()
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
            if MAP[ty][tx] != 0 and not check[ty][tx]:
                check[ty][tx] = True
                MAP[ty][tx] = num
                Q.append([ty, tx])


def is_all_connected():
    global count
    # print(connect)
    Q = deque()
    V = [0 for _ in range(count + 1)]
    if len(connect[1]) != 0:
        Q.append(1)
        V[1] = 1
        while Q:
            s = Q.popleft()
            for w in connect[s]:
                if V[w]: continue
                V[w] = 1
                Q.append(w)

    if sum(V) == count:
        return True
    else:
        return False


def dfs(y, x):
    global min_len
    global totlen
    visited = [[False for _ in range(C)] for _ in range(R)]
    if is_all_connected():
        # print(connect)
        # print(totlen)
        min_len = min(totlen, min_len)
        return

    if x == C:
        x, y = 0, y + 1

    if y == R:
        return

    # print(y, x, totlen)
    if MAP[y][x] == 0:
        dfs(y, x + 1)
    if MAP[y][x] != 0 and not visited[y][x]:
        visited[y][x] = True
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
            if MAP[ty][tx] == MAP[y][x]: continue
            if MAP[ty][tx] == 0:
                length = 1
                while True:
                    ty += dy[dir]
                    tx += dx[dir]
                    if ty < 0 or ty >= R or tx < 0 or tx >= C: break
                    if MAP[ty][tx] == 0:
                        length += 1
                        continue
                    if MAP[ty][tx] not in connect[MAP[y][x]]:
                        if length > 1:
                            connect[MAP[y][x]].append(MAP[ty][tx])
                            connect[MAP[ty][tx]].append(MAP[y][x])
                            totlen += length
                            dfs(y, x + 1)
                            connect[MAP[y][x]].pop()
                            connect[MAP[ty][tx]].pop()
                            totlen -= length
                    else: break

        dfs(y, x + 1)



R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
check = [[False for _ in range(C)] for _ in range(R)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]

count = 0
for i in range(R):
    for j in range(C):
        if MAP[i][j] != 0 and not check[i][j]:
            count += 1
            bfs(i, j, count)

connect = [[] for _ in range(count + 1)]
min_len = 0xfffff
totlen = 0
dfs(0, 0)

if min_len == 0xfffff:
    print(-1)
else:
    print(min_len)
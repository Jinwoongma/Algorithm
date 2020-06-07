from _collections import deque
from queue import PriorityQueue


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


def MST_PRIM(G, r):
    Q = PriorityQueue()
    D = [0xfffff] * (count + 1)
    visited = [False] * (count + 1)
    D[r] = 0
    Q.put([0, r])

    while not Q.empty():
        d, u = Q.get()
        visited[u] = True

        for w in G[u]:
            v, l = w[0], w[1]
            if not visited[v] and l < D[v]:
                D[v] = l
                Q.put([D[v], v])

    ret = 0
    for i in range(1, count + 1):
        ret += D[i]
    return ret


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

G = [[] for _ in range(count + 1)]
for i in range(R):
    for j in range(C):
        if MAP[i][j] != 0:
            for dir in range(4):
                ty, tx = i + dy[dir], j + dx[dir]
                if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
                if MAP[ty][tx] == 0:
                    tty, ttx, l = ty, tx, 1
                    while True:
                        tty += dy[dir]
                        ttx += dx[dir]
                        if tty < 0 or tty >= R or ttx < 0 or ttx >= C: break
                        if MAP[tty][ttx] == 0:
                            l += 1
                            continue
                        else:
                            if l > 1:
                                flag = True
                                for k in range(len(G[MAP[i][j]])):
                                    path = G[MAP[i][j]][k]
                                    if MAP[tty][ttx] == path[0]:
                                        if l <= path[1]:
                                            G[MAP[i][j]][k] = [MAP[tty][ttx], l]
                                            flag = False
                                        else:
                                            continue
                                if flag:
                                    G[MAP[i][j]].append([MAP[tty][ttx], l])
                            break

result = MST_PRIM(G, 1)
if result >= 0xfffff:
    print(-1)
else:
    print(result)

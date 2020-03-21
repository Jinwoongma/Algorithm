from copy import deepcopy
import sys
sys.setrecursionlimit(1000000)


def dfs(y, x):
    global flag, path
    outside[y][x] = True

    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= R or tx < 0 or tx >= C:
            flag = True
            continue
        if not outside[ty][tx] and MAP[ty][tx] == 0:
            path.append([ty, tx])
            dfs(ty, tx)


R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
time = 0

while True:
    outside = [[False for _ in range(C)] for _ in range(R)]
    new_MAP = deepcopy(MAP)
    path = [[0, 0]]
    dfs(0, 0)
    for k in range(len(path)):
        new_MAP[path[k][0]][path[k][1]] = 2

    visited = [[False for _ in range(C)] for _ in range(R)]
    DEL = []
    for i in range(R):
        for j in range(C):
            if new_MAP[i][j] == 1:
                cnt = 0
                for dir in range(4):
                    ty, tx = i + dy[dir], j + dx[dir]
                    if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
                    if new_MAP[ty][tx] == 2:
                        cnt += 1
                if cnt >= 2:
                    DEL.append([i, j])

    for i in range(len(DEL)):
        MAP[DEL[i][0]][DEL[i][1]] = 0

    time += 1

    tot = 0
    for i in range(R):
        tot += sum(MAP[i])

    if tot == 0:
        print(time)
        break

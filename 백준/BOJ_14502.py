import copy
from collections import deque

def combination(k, s):
    if k == 3:
        temp = []
        for i in range(3):
            temp.append(zeros[pick[i]])
        comb_results.append(temp)
    else:
        for i in range(s, zero_count):
            pick[k] = i
            combination(k+1, i+1)

row, col = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(row)]
zeros = []
birus = []
comb_results = []
pick = [0] * 3
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]
Q = deque()

for r in range(row):
    for c in range(col):
        if MAP[r][c] == 0:
            zeros.append((r, c))
        if MAP[r][c] == 2:
            birus.append((r, c))
zero_count = len(zeros)
birus_count = len(birus)
combination(0, 0)

max_safe = 0
for result in comb_results:
    new_MAP = copy.deepcopy(MAP)
    for coor in result:
        new_MAP[coor[0]][coor[1]] = 1
    for i in range(birus_count):
        Q.append(birus[i])
    visited = [[False for _ in range(col)] for _ in range(row)]
    D = [[0 for _ in range(col)] for _ in range(row)]
    path = 0
    while len(Q) != 0:
        loop_size = len(Q)
        for i in range(loop_size):
            v = Q.popleft()
            y, x = v[0], v[1]
            for dir in range(4):
                ty, tx = y + dy[dir], x + dx[dir]
                if ty >= 0 and ty < row and tx >= 0 and tx < col:
                    if not visited[ty][tx] and new_MAP[ty][tx] == 0:
                        new_MAP[ty][tx] = 2
                        visited[ty][tx] = True
                        Q.append((ty, tx))

    safe = 0
    for i in range(row):
        for j in range(col):
            if new_MAP[i][j] == 0:
                safe += 1
    if max_safe <= safe:
        max_safe = safe
print(max_safe)

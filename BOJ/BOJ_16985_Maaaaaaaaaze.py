from _collections import deque
from itertools import permutations

def turn(floor, rep):
    for i in range(5):
        for j in range(5):
            if rep == 0: change_MAP[floor][i][j] = MAP[floor][i][j]
            elif rep == 1: change_MAP[floor][i][j] = MAP[floor][4 - j][i]
            elif rep == 2: change_MAP[floor][i][j] = MAP[floor][4 - i][4 - j]
            else: change_MAP[floor][i][j] = MAP[floor][j][4 - i]


def bfs():
    visited = [[[False for _ in range(5)] for _ in range(5)] for _ in range(5)]

    if not change_MAP[0][0][0] or not change_MAP[4][4][4]:
        return 0xfffff
    Q = deque()
    Q.append([0, 0, 0, 0])
    visited[0][0][0] = True
    while Q:
        h, y, x, d = Q.popleft()
        if h == 4 and y == 4 and x == 4:
            return d
        for dir in range(6):
            th, ty, tx = h + dh[dir], y + dy[dir], x + dx[dir]
            if 0 <= th < 5 and 0 <= ty < 5 and 0 <= tx < 5:
                if not visited[th][ty][tx] and change_MAP[th][ty][tx] == 1:
                    visited[th][ty][tx] = True
                    Q.append([th, ty, tx, d + 1])
    return 0xfffff


def dfs(floor):
    global ans
    if floor == 5:
        for i in range(5):
            turn(i, floor_check[i])
        ans = min(ans, bfs())
        return
    for rep in range(4):
        floor_check[floor] = rep
        dfs(floor + 1)


maze = []
for i in range(5):
    maze.append([list(map(int, input().split())) for _ in range(5)])
dh = [-1, 1, 0, 0, 0, 0]; dy = [0, 0, -1, 1, 0, 0]; dx = [0, 0, 0, 0, -1, 1]
ans = 0xfffff

for perms in permutations(range(5), 5):
    MAP = []
    for i in range(5):
        MAP.append(maze[perms[i]])
    change_MAP = [[[0 for _ in range(5)] for _ in range(5)] for _ in range(5)]
    floor_check = [0 for _ in range(5)]
    dfs(0)

if ans == 0xfffff:
    print(-1)
else:
    print(ans)
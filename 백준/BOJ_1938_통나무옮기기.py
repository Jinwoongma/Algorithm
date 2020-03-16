from _collections import deque

N = int(input())
MAP = [list(map(str, input().strip())) for _ in range(N)]
visited = [[[0 for _ in range(2)] for _ in range(N)] for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
tree, end = [], []
min_result = 0xfffff

for i in range(N):
    for j in range(N):
        if MAP[i][j] == 'B':
            tree.append([i, j])
            MAP[i][j] = 0
        elif MAP[i][j] == 'E':
            end.append([i, j])
            MAP[i][j] = 0
        else:
            MAP[i][j] = int(MAP[i][j])

Q = deque()
if tree[0][0] == tree[1][0]:
    Q.append([tree[1], 0, 0])  # 0: 누운 상태, 1: 선 상태
    visited[tree[1][0]][tree[1][1]][0] = True
elif tree[0][1] == tree[1][1]:
    Q.append([tree[1], 1, 0])
    visited[tree[1][0]][tree[1][1]][1] = True

if end[0][0] == end[1][0]:
    e = [end[1], 0]
elif end[0][1] == end[1][1]:
    e = [end[1], 1]


while Q:
    center, dir, cnt = Q.popleft()
    y, x = center[0], center[1]

    if center == e[0] and dir == e[1]:
        min_result = cnt
        break

    for d in range(4):
        ty, tx = y + dy[d], x + dx[d]
        if dir == 0:
            if ty < 0 or ty >= N or tx < 1 or tx >= N - 1: continue
            if MAP[ty][tx - 1] == 0 and MAP[ty][tx] == 0 and MAP[ty][tx + 1] == 0 and not visited[ty][tx][0]:
                visited[ty][tx][0] = True
                Q.append([[ty, tx], 0, cnt + 1])
        elif dir == 1:
            if ty < 1 or ty >= N - 1 or tx < 0 or tx >= N: continue
            if MAP[ty - 1][tx] == 0 and MAP[ty][tx] == 0 and MAP[ty + 1][tx] == 0 and not visited[ty][tx][1]:
                visited[ty][tx][1] = True
                Q.append([[ty, tx], 1, cnt + 1])

    if 1 <= y <= N - 2 and 1 <= x <= N - 2:
        flag = True
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if MAP[i][j] == 1:
                    flag = False
        if flag:
            if not visited[y][x][abs(dir - 1)]:
                visited[y][x][abs(dir - 1)] = True
                Q.append([[y, x], abs(dir - 1), cnt + 1])

if min_result == 0xfffff:
    print(0)
else:
    print(min_result)
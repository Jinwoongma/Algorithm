from _collections import deque

def bfs(y, x, ref):
    global path
    Q = deque()
    Q.append([y, x])
    visited[y][x] = True
    while Q:
        y, x = Q.popleft()
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= 12 or tx < 0 or tx >= 6: continue
            if MAP[ty][tx] == ref and not visited[ty][tx]:
                visited[ty][tx] = True
                path += [[ty, tx]]
                Q.append([ty, tx])


def pulldown(arr):
    for i in range(6):
        Q = []
        for j in range(12):
            if arr[j][i] != '.':
                Q.append(arr[j][i])
        for j in range(11, -1, -1):
            if Q:
                arr[j][i] = Q.pop()
            else:
                arr[j][i] = '.'
    return arr


MAP = [list(input().strip()) for _ in range(12)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
score = 0
while True:
    visited = [[False for _ in range(6)] for _ in range(12)]
    del_path = []
    for i in range(12):
        for j in range(6):
            if MAP[i][j] != '.' and not visited[i][j]:
                path = [[i, j]]
                bfs(i, j, MAP[i][j])
                if len(path) >= 4:

                    del_path += path

    if len(del_path) == 0:
        break

    score += 1
    for i in range(len(del_path)):
        MAP[del_path[i][0]][del_path[i][1]] = '.'

    pulldown(MAP)


print(score)
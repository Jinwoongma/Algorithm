from _collections import deque

def bfs(sy, sx):
    global key, result

    Q = deque()
    Q.append([sy, sx])
    visited[sy][sx] = True
    while Q:
        y, x = Q.popleft()
        # print(Q)
        # print(door, key)
        # print(y, x)
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= r + 2 or tx < 0 or tx >= c + 2: continue
            if MAP[ty][tx] == '.' and not visited[ty][tx]:
                if ty != 0 and tx != 0 and ty != r + 1 and tx != c + 1:
                    visited[ty][tx] = True
                    Q.append([ty, tx])

            if ord('A') <= ord(MAP[ty][tx]) <= ord('Z') and not visited[ty][tx]:
                if MAP[ty][tx].lower() in key:
                    visited[ty][tx] = True
                    Q.append([ty, tx])
                else:
                    if MAP[ty][tx] in door:
                        door[MAP[ty][tx]].append([ty, tx])
                    else:
                        door[MAP[ty][tx]] = [[ty, tx]]

            if ord('a') <= ord(MAP[ty][tx]) <= ord('z') and not visited[ty][tx]:
                if MAP[ty][tx].upper() not in door:
                    key += MAP[ty][tx]
                    visited[ty][tx] = True
                    Q.append([ty, tx])
                else:
                    visited[ty][tx] = True
                    Q.append([ty, tx])
                    key += MAP[ty][tx]
                    for i in range(len(door[MAP[ty][tx].upper()])):
                        ny, nx = door[MAP[ty][tx].upper()][i][0], door[MAP[ty][tx].upper()][i][1]
                        if not visited[ny][nx]:
                            visited[ny][nx] = True
                            Q.append([ny, nx])
                    del door[MAP[ty][tx].upper()]

            if MAP[ty][tx] == '$' and not visited[ty][tx]:
                visited[ty][tx] = True
                Q.append([ty, tx])
                result += 1


TC = int(input())
for tc in range(TC):
    r, c = map(int, input().split())
    MAP = [['.'] + list(map(str, input().strip())) + ['.'] for _ in range(r)]
    MAP = [['.' for _ in range(c + 2)]] + MAP + [['.' for _ in range(c + 2)]]

    key = str(input())
    if key == '0':
        key = ''
    door = {}
    visited = [[False for _ in range(c + 2)] for _ in range(r + 2)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    result = 0

    for i in range(r + 2):
        for j in range(c + 2):  
            if i == 0 or j == 0 or i == r + 1 or j == c + 1:
                if MAP[i][j] == '.' and not visited[i][j]:
                    bfs(i, j)

    print(result)
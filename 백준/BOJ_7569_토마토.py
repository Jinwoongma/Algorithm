from _collections import deque
C, R, H = map(int, input().split())
MAP = [[list(map(int, input().split())) for _ in range(R)] for _ in range(H)]
visited = [[[False for _ in range(C)] for _ in range(R)] for _ in range(H)]
dy = [-1, 1, 0, 0, 0, 0]  # 상, 하, 좌, 우, 위, 아래
dx = [0, 0, -1, 1, 0, 0]
dh = [0, 0, 0, 0, -1, 1]

def check(arr):
    for h in range(H):
        for y in range(R):
            for x in range(C):
                if arr[h][y][x] == 0:
                    return False
    return True

def find_ripe():
    new_arr = []
    for i in range(H):
        for j in range(R):
            for k in range(C):
                if MAP[i][j][k] == 1: Q.append([i, j, k])
    return new_arr

Q = deque()
find_ripe()
day = -1

while Q:
    day += 1
    for i in range(len(Q)):
        s = Q.popleft()
        h, y, x = s[0], s[1], s[2]
        for dir in range(6):
            th, ty, tx = h + dh[dir], y + dy[dir], x + dx[dir]
            if th < 0 or th >= H or ty < 0 or ty >= R or tx < 0 or tx >= C:
                continue
            if MAP[th][ty][tx] == -1 or MAP[th][ty][tx] == 1: continue
            if MAP[th][ty][tx] == 0 and not visited[th][ty][tx]:
                MAP[th][ty][tx] = 1
                visited[th][ty][tx] = True
                Q.append([th, ty, tx])

if check(MAP): print(day)
else: print(-1)

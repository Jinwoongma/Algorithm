from _collections import deque

def bfs(y, x):
    Q = deque()
    Q.append([y, x])
    visited[y][x] = True
    ret = 1
    while Q:
        y, x = Q.popleft()
        for dir in range(4):
            if MAP[y][x] & (1 << dir) == 0:
                ty, tx = y + dy[dir], x + dx[dir]
                if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
                if not visited[ty][tx]:
                    visited[ty][tx] = True
                    ret += 1
                    Q.append([ty, tx])
    return ret


C, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
visited = [[False for _ in range(C)] for _ in range(R)]
dy = [0, -1, 0, 1]; dx = [-1, 0, 1, 0]  # 서, 북, 동, 남

room_cnt = 0
max_area, max_area2 = -1, -1
for i in range(R):
    for j in range(C):
        if not visited[i][j]:
            room_cnt += 1
            ret = bfs(i, j)
            max_area = max(max_area, ret)

for i in range(R):
    for j in range(C):
        for dir in range(4):
            if MAP[i][j] & (1 << dir) != 0:
                visited = [[False for _ in range(C)] for _ in range(R)]
                MAP[i][j] -= (1 << dir)
                max_area2 = max(max_area2, bfs(i, j))
                MAP[i][j] += (1 << dir)

print(room_cnt)
print(max_area)
print(max_area2)

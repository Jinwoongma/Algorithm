from itertools import permutations
from _collections import deque

def bfs(sy, sx, ey, ex):
    Q = deque()
    visited = [[False for _ in range(C)] for _ in range(R)]
    Q.append([sy, sx, 0])
    visited[sy][sx] = True
    while Q:
        y, x, d = Q.popleft()
        if y == ey and x == ex:
            break
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
            if MAP[ty][tx] != '#' and not visited[ty][tx]:
                visited[ty][tx] = True
                Q.append([ty, tx, d + 1])
    return d


C, R = map(int, input().split())
MAP = [list(map(str, input().strip())) for _ in range(R)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
result = 0xfffff
items = []
item_cnt = 0

for i in range(R):
    for j in range(C):
        if MAP[i][j] == 'X':
            items.append([i, j])
            item_cnt += 1
        if MAP[i][j] == 'S':
            sy, sx = i, j
        if MAP[i][j] == 'E':
            ey, ex = i, j

for perms in permutations(range(item_cnt), item_cnt):
    sub_result = 0
    if item_cnt == 0:
        sub_result += bfs(sy, sx, ey, ex)
    else:
        for i in range(item_cnt + 1):
            if i == 0:
                start_y, start_x = sy, sx
                end_y, end_x = items[perms[0]]
            elif i == item_cnt:
                start_y, start_x = items[perms[item_cnt - 1]]
                end_y, end_x = ey, ex
            else:
                start_y, start_x = items[perms[i - 1]]
                end_y, end_x = items[perms[i]]
            sub_result += bfs(start_y, start_x, end_y, end_x)
    result = min(result, sub_result)

print(result)

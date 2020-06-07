from _collections import deque
from copy import deepcopy

N = int(input())
MAP = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[False for _ in range(N**2)] for _ in range(N)] for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
ans = 0xfffff

Q = deque()
Q.append([0, 0, 0])
visited[0][0][0] = True
while Q:
    y, x, break_cnt = Q.popleft()
    if y == N - 1 and x == N - 1:
        ans = min(ans, break_cnt)
        continue

    if break_cnt >= ans:
        continue

    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
        if MAP[ty][tx] == 1:
            if not visited[ty][tx][break_cnt]:
                visited[ty][tx][break_cnt] = True
                Q.append([ty, tx, break_cnt])
        else:
            if not visited[ty][tx][break_cnt + 1]:
                visited[ty][tx][break_cnt + 1] = True
                Q.append([ty, tx, break_cnt + 1])

print(ans)
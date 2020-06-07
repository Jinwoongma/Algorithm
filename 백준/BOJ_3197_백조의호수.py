import sys
from _collections import deque

def bfs(arr):
    global MAX
    P = deque(arr)
    while P:
        y, x, d = P.popleft()
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
            if MAP[ty][tx] == 'X' and D[ty][tx] == 0:
                D[ty][tx] = d + 1
                MAX = max(MAX, d + 1)
                P.append([ty, tx, d + 1])


def IsConnected(mid, index):
    Q = deque()
    Q.append([swan[0][0], swan[0][1]])
    while Q:
        y, x = Q.popleft()
        if y == swan[1][0] and x == swan[1][1]: return True
        visited[y][x] = index
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= R or tx < 0 or tx >= C or visited[ty][tx] >= index: continue
            if D[ty][tx] <= mid:
                visited[ty][tx] = index
                Q.append([ty, tx])
    return False


R, C = map(int, input().split())
MAP = [list(map(str, sys.stdin.readline().strip())) for i in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
swan = []
D = [[0 for _ in range(C)] for _ in range(R)]
P = deque()
for i in range(R):
    for j in range(C):
        if MAP[i][j] == 'L':
            swan.append([i, j])
            P.append([i, j, 0])
        elif MAP[i][j] == '.':
            P.append([i, j, 0])

MAX = 0
bfs(P)
answer = 0xfffff
lo, hi = 0, MAX
t = 0
while lo <= hi:
    t += 1
    mid = (lo + hi) // 2
    if IsConnected(mid, t):
        answer = min(answer, mid)
        hi = mid - 1
    else:
        lo = mid + 1
print(answer)
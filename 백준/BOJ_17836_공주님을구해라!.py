from _collections import deque

def bfs(y, x):
    global ans
    Q = deque()
    Q.append([y, x, 0, 0])
    visited[y][x][0] = True
    while Q:
        y, x, gram, cnt = Q.popleft()
        if cnt > T:
            return
        if y == R - 1 and x == C - 1:
            ans = cnt
            return
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
            if gram == 0:
                if not visited[ty][tx][0] and MAP[ty][tx] != 1:

                    if MAP[ty][tx] == 2:
                        visited[ty][tx][1] = True
                        Q.append([ty, tx, 1, cnt + 1])
                    else:
                        visited[ty][tx][0] = True
                        Q.append([ty, tx, 0, cnt + 1])
            else:
                if not visited[ty][tx][1]:
                    visited[ty][tx][1] = True
                    Q.append([ty, tx, 1, cnt + 1])


R, C, T = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
visited = [[[False for _ in range(2)] for _ in range(C)] for _ in range(R)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
ans = False
bfs(0, 0)
if not ans:
    print("Fail")
else:
    print(ans)
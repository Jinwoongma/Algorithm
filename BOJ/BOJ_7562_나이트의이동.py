from _collections import deque

TC = int(input())
for tc in range(TC):
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]
    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    L = int(input())
    visited = [[False for _ in range(L)] for _ in range(L)]
    sy, sx = map(int, input().split())
    ey, ex = map(int, input().split())

    Q = deque()
    Q.append([sy, sx, 0])
    visited[sy][sx] = True
    while Q:
        y, x, cnt = Q.popleft()
        if y == ey and x == ex:
            print(cnt)
            break
        for dir in range(8):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= L or tx < 0 or tx >= L: continue
            if not visited[ty][tx]:
                visited[ty][tx] = True
                Q.append([ty, tx, cnt + 1])

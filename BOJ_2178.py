from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
N, M = map(int, input().split())
miro = [str(input()) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
D = [[0 for _ in range(M)] for _ in range(N)]
result = []

def is_range(y, x):
    if x >= 0 and x < M and y >= 0 and y < N:
        return True
    else:
        return False

def bfs(y, x):
    Q = deque()
    Q.append((y, x))

    while Q:
        v = Q.popleft()
        y, x = v[0], v[1]
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if is_range(ty, tx):
                if not visited[ty][tx] and miro[ty][tx] == '1':
                    D[ty][tx] = D[y][x] + 1
                    visited[ty][tx] = True
                    Q.append((ty, tx))
    return D

D = bfs(0, 0)
print(D[N-1][M-1]+1)
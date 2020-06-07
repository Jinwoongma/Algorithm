from collections import deque
N, M = map(int, input().split())
maze = [input() for _ in range(N)]
visit = [[0] * M for _ in range(N)]
D = [[0] * M for _ in range(N)]  # 거리 저장
dx = [0, 0, -1, 1]; dy = [1, -1, 0, 0]

def BFS(y, x):
    Q = deque()
    Q.append((x, y))
    visit[y][x] = 1
    while(Q):
        y, x = Q.popleft()
        for i in range(4):
            tx, ty = x + dx[i], y + dy[i]
            if tx < 0 or tx == N or ty < 0 or ty == M: continue
            if maze[ty][tx] == '0' or visit[ty][tx]: continue
            visit[ty][tx] = 1
            D[ty][tx] = D[y][x] + 1
            Q.append((ty, tx))
    return D

D = BFS(0, 0)
print(D[N-1][M-1]+1)
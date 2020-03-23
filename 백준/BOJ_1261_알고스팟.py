import heapq

C, R = map(int, input().split())
MAP = [list(map(int, input().strip())) for _ in range(R)]
D = [[0xfffff for _ in range(C)] for _ in range(R)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]

h = []
D[0][0] = 0
heapq.heappush(h, (0, 0))
while h:
    y, x = heapq.heappop(h)
    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
        if MAP[ty][tx] == 0 and D[ty][tx] > D[y][x]:
            D[ty][tx] = D[y][x]
            heapq.heappush(h, (ty, tx))
        if MAP[ty][tx] == 1 and D[ty][tx] > D[y][x] + 1:
            D[ty][tx] = D[y][x] + 1
            heapq.heappush(h, (ty, tx))

print(D[R - 1][C - 1])
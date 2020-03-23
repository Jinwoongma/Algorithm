import heapq

TC = 0
while True:
    TC += 1
    N = int(input())
    if N == 0:
        break
    MAP = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    D = [[0xfffff for _ in range(N)] for _ in range(N)]
    h = []
    D[0][0] = MAP[0][0]
    heapq.heappush(h, (D[0][0], 0, 0))
    while h:
        d, y, x = heapq.heappop(h)
        if d < D[y][x]: continue
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
            if D[ty][tx] > D[y][x] + MAP[ty][tx]:
                D[ty][tx] = D[y][x] + MAP[ty][tx]
                heapq.heappush(h, (d + MAP[ty][tx], ty, tx))

    print('Problem {}: {}'.format(TC, D[N - 1][N - 1]))
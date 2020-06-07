def solve(head, shape):
    global answer

    hy, hx = head // N, head % N
    if hy == N - 1 and hx == N - 1:
        answer += 1
        return

    if shape == 0:
        if hx + 1 < N and MAP[hy][hx + 1] == 0:
            nhy, nhx = hy, hx + 1
            solve(nhy * N + nhx, 0)
        if (hy + 1 < N and hx + 1 < N) and (MAP[hy + 1][hx + 1] == 0 and MAP[hy + 1][hx] == 0 and MAP[hy][hx + 1] == 0):
            nhy, nhx = hy + 1, hx + 1
            solve(nhy * N + nhx, 2)
    if shape == 1:
        if hy + 1 < N and MAP[hy + 1][hx] == 0:
            nhy, nhx = hy + 1, hx
            solve(nhy * N + nhx, 1)
        if (hy + 1 < N and hx + 1 < N) and (MAP[hy + 1][hx + 1] == 0 and MAP[hy + 1][hx] == 0 and MAP[hy][hx + 1] == 0):
            nhy, nhx = hy + 1, hx + 1
            solve(nhy * N + nhx, 2)
    if shape == 2:
        if hy + 1 < N and MAP[hy + 1][hx] == 0:
            nhy, nhx = hy + 1, hx
            solve(nhy * N + nhx, 1)
        if hx + 1 < N and MAP[hy][hx + 1] == 0:
            nhy, nhx = hy, hx + 1
            solve(nhy * N + nhx, 0)
        if (hy + 1 < N and hx + 1 < N) and (MAP[hy + 1][hx + 1] == 0 and MAP[hy + 1][hx] == 0 and MAP[hy][hx + 1] == 0):
            nhy, nhx = hy + 1, hx + 1
            solve(nhy * N + nhx, 2)


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
answer = 0
solve(1, 0)
print(answer)
TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    A = [0] * (N**2 + 1)
    max_length = 0

    for i in range(N):
        for j in range(N):
            for dir in range(4):
                ty, tx = i + dy[dir], j + dx[dir]
                if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
                if MAP[ty][tx] - MAP[i][j] == 1:
                    A[MAP[i][j]] = 1
    # print(A)

    length = 0
    start_idx = 0
    for i in range(N**2, -1, -1):
        if A[i] == 1:
            length += 1
        else:
            if max_length <= length:
                max_length = length
                start_idx = i + 1
            length = 0

    print('#{} {} {}'.format(tc + 1, start_idx, max_length + 1))
import sys
sys.stdin = open("폭격작전2_input.txt", "r")

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    bomb = [[0 for _ in range(N)] for _ in range(N)]

    for m in range(M):
        y, x, range_ = map(int, input().split())
        for row in range(y, y+range_):
            if row >= N:
                break
            for col in range(x, x+range_):
                if col >= N:
                    break
                bomb[row][col] = 1

    sum_ = 0
    for i in range(N):
        for j in range(N):
            if bomb[i][j] == 1:
                sum_ += MAP[i][j]

    print('#{} {}'.format(tc+1, sum_))
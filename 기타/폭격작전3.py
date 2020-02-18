import sys
sys.stdin = open("폭격작전3_input.txt", "r")

def change(row, col):
    for i in range(N):
        bomb[row][i] = 1
        bomb[i][col] = 1

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    bomb = [[0 for _ in range(N)] for _ in range(N)]

    for m in range(M):
        row, col = map(int, input().split())
        change(row, col)

    sum_ = 0
    for i in range(N):
        for j in range(N):
            if bomb[i][j] == 1:
                sum_ += data[i][j]
    print('#{} {}'.format(tc + 1, sum_))
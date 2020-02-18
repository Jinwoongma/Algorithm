import sys
sys.stdin = open("폭격작전4_input.txt", "r")

def change(row, col, range_):
    bomb[row][col] = 1
    for i in range(1, range_ + 1):
        if row - i >= 0:
            bomb[row - i][col] = 1
        if row + i < N:
            bomb[row + i][col] = 1
        if col - i >= 0:
            bomb[row][col - i] = 1
        if col + i < N:
            bomb[row][col + i] = 1

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    bomb = [[0 for _ in range(N)] for _ in range(N)]
    for m in range(M):
        row, col, range_ = map(int, input().split())
        change(row, col, range_)

    sum_ = 0
    for i in range(N):
        for j in range(N):
            if bomb[i][j] == 1:
                sum_ += data[i][j]
    print('#{} {}'.format(tc+1, sum_))
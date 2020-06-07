import sys
sys.stdin = open('가로세로폭탄_input.txt', 'r')

def cal(row, col, data):
    row_sum, col_sum = 0, 0
    for i in range(N):
        row_sum += data[row][i]
        col_sum += data[i][col]
    return row_sum + col_sum - data[row][col]

TC = int(input())
for tc in range(TC):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    max_row, max_col, max_result = 0, 0, 0

    for i in range(N):
        for j in range(N):
            result = cal(i, j, data)
            if result >= max_result:
                max_result = result
                max_row = i
                max_col = j
    print('#{} {} {} {}'.format(tc+1, max_row, max_col, max_result))

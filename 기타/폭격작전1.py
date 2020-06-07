import sys
sys.stdin = open('폭격작전1_input.txt', 'r')
TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    new_data = [[0 for _ in range(N+1)] for _ in range(N+1)]
    max_result, max_row, max_col = 0, 0, 0

    for i in range(0, N):
        new_data[i+1][1] = data[i][0]
        for j in range(1, N):
            new_data[i+1][j+1] = new_data[i+1][j] + data[i][j]

    for i in range(2, N+1):
        for j in range(1, N+1):
            new_data[i][j] += new_data[i-1][j]

    for i in range(M, N+1):
        for j in range(M, N+1):
            result = new_data[i][j] - new_data[i-M][j] - new_data[i][j-M] + new_data[i-M][j-M]
            if max_result <= result:
                max_result = result
                max_row = i - M
                max_col = j - M

    print('#{} {} {} {}'.format(tc+1, max_row, max_col, max_result))
import sys
sys.stdin = open('대각폭탄_input.txt', 'r')

TC = int(input())
for tc in range(TC):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, 1, 1, -1]  #위오, 아래오, 아래왼, 위왼
    dx = [1, 1, -1, -1]

    max_sum, max_row, max_col = 0, 0, 0
    for y in range(N):
        for x in range(N):
            sum_ = data[y][x]
            for dir in range(4):
                ty, tx = y + dy[dir], x + dx[dir]
                while True:
                    if ty < 0 or ty == N or tx < 0 or tx == N:
                        break
                    sum_ += data[ty][tx]
                    ty, tx = ty + dy[dir], tx + dx[dir]

            if max_sum <= sum_:
                max_sum = sum_
                max_row, max_col = y, x

    print('#{} {} {} {}'.format(tc+1, max_row, max_col, max_sum))
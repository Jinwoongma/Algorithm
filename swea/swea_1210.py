import copy
import sys
sys.stdin = open('input_1210.txt', 'r')

for tc in range(1, 11):
    t = int(input())
    dy = [0, 0, 1]
    dx = [1, -1, 0]  # 우 -> 좌 -> 상
    MAP = [list(map(int, input().split())) for _ in range(100)]
    start = [i for i in range(100) if MAP[0][i] == 1]

    for s in start:
        y, x = 0, s
        temp = copy.deepcopy(MAP)

        while y <= 99:
            if y == 99:
                if temp[y][x] == 2:
                    print('#{} {}'.format(t, s))
                    break
                break

            for dir in range(3):
                ty = y + dy[dir]; tx = x + dx[dir]
                if ty < 0 or ty == 100 or tx < 0 or tx == 100:
                    continue
                if temp[ty][tx] == 0:
                    continue
                else:
                    temp[y][x] = 0
                    y, x = ty, tx
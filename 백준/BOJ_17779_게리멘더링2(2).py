# 21:42 ~ 23:18

def fill(MAP):
    for i in range(1, N + 1):
        flag = False
        temp = []
        for j in range(1, N + 1):
            if MAP[i][j] == 1:
                if not flag:
                    flag = True
                else:
                    flag = False
            else:
                if flag: temp.append([i, j])
        if not flag:
            for r, c in temp:
                MAP[r][c] = 1

N = int(input())
COST = [list(map(int, input().split())) for _ in range(N)]
answer = 0xfffff

for y in range(1, N):
    for x in range(1, N):
        for d1 in range(1, N + 1):
            for d2 in range(1, N + 1):
                if (x < x + d1 + d2 <= N) and (1 <= y - d1 < y < y + d2 <= N):
                    MAP = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
                    ty, tx = y, x
                    for i in range(d1 + 1):
                        MAP[ty][tx] = 1
                        ty -= 1; tx += 1

                    ty, tx = y, x
                    for i in range(d2 + 1):
                        MAP[ty][tx] = 1
                        ty += 1; tx += 1

                    ty, tx = y - d1, x + d1
                    for i in range(d2 + 1):
                        MAP[ty][tx] = 1
                        ty += 1;  tx += 1

                    ty, tx = y + d2, x + d2
                    for i in range(d1 + 1):
                        MAP[ty][tx] = 1
                        ty -= 1; tx += 1

                    fill(MAP)

                    result = [0, 0, 0, 0, 0]
                    for i in range(1, N + 1):
                        for j in range(1, N + 1):
                            if j <= x + d1 and i < y and MAP[i][j] != 1:
                                result[0] += COST[i - 1][j - 1]

                            elif j > x + d1 and i <= y - d1 + d2 and MAP[i][j] != 1:
                                result[1] += COST[i - 1][j - 1]

                            elif j < x + d2 and i >= y and MAP[i][j] != 1:
                                result[2] += COST[i - 1][j - 1]


                            elif j >= x + d2 and i > y - d1 + d2 and MAP[i][j] != 1:
                                result[3] += COST[i - 1][j - 1]

                            elif MAP[i][j] == 1:
                                result[4] += COST[i - 1][j - 1]

                    answer = min(answer, max(result) - min(result))
# SUM = 0
# for i in range(N):
#     SUM += sum(COST[i])
# print(SUM)
print(answer)
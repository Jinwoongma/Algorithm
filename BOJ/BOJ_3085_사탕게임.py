N = int(input())
MAP = [list(map(str, input().strip())) for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
max_cnt = 1

for i in range(N):
    for j in range(N):
        # 좌/우 스왑
        if j != N - 1:
            MAP[i][j], MAP[i][j + 1] = MAP[i][j + 1], MAP[i][j]
            ref, l = MAP[0][j], 1
            for k in range(1, N):
                if MAP[k][j] == ref:
                    l += 1
                    max_cnt = max(max_cnt, l)
                else:
                    ref, l = MAP[k][j], 1

            ref, l = MAP[0][j + 1], 1
            for k in range(1, N):
                if MAP[k][j + 1] == ref:
                    l += 1
                    max_cnt = max(max_cnt, l)
                else:
                    ref, l = MAP[k][j + 1], 1

            ref, l = MAP[i][0], 1
            for k in range(1, N):
                if MAP[i][k] == ref:
                    l += 1
                    max_cnt = max(max_cnt, l)
                else:
                    ref, l = MAP[i][k], 1

            MAP[i][j], MAP[i][j + 1] = MAP[i][j + 1], MAP[i][j]


        # 상/하 스왑
        if i != N - 1:
            MAP[i][j], MAP[i + 1][j] = MAP[i + 1][j], MAP[i][j]
            ref, l = MAP[i][0], 1
            for k in range(1, N):
                if MAP[i][k] == ref:
                    l += 1
                    max_cnt = max(max_cnt, l)
                else:
                    ref, l = MAP[i][k], 1

            ref, l = MAP[i + 1][0], 1
            for k in range(1, N):
                if MAP[i + 1][k] == ref:
                    l += 1
                    max_cnt = max(max_cnt, l)
                else:
                    ref, l = MAP[i + 1][k], 1

            ref, l = MAP[0][j], 1
            for k in range(1, N):
                if MAP[k][j] == ref:
                    l += 1
                    max_cnt = max(max_cnt, l)
                else:
                    ref, l = MAP[k][j], 1
            MAP[i][j], MAP[i + 1][j] = MAP[i + 1][j], MAP[i][j]

print(max_cnt)
N = int(input())
MAP = [[0] * (N + 1)] + [[0] + list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
min_diff = 0xffffffff

arr = []
for i in range(1, N + 1):  # x
    for j in range(1, N + 1):  # y
        for k in range(1, N + 1):  # d1
            for m in range(1, N + 1):  # d2
                if j + k + m <= N and 1 <= i - k <= i + m <= N:
                    arr.append([i, j, k, m])

SUM = 0
for r in range(N + 1):
    for c in range(N + 1):
        SUM += MAP[r][c]

lines = []
for i in range(len(arr)):
    line = []
    x, y, d1, d2 = arr[i]
    for i in range(d1 + 1):
        ty, tx = y + i, x - i
        line.append([ty, tx])
    for i in range(d2 + 1):
        ty, tx = y + i, x + i
        line.append([ty, tx])
    for i in range(d2 + 1):
        ty, tx = y + d1 + i, x - d1 + i
        line.append([ty, tx])
    for i in range(d1 + 1):
        ty, tx = y + d2 + i, x + d2 - i
        line.append([ty, tx])

    temp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for j in range(len(line)):
        temp[line[j][0]][line[j][1]] = 1

    for r in range(1, N + 1):
        flag = False
        for c in range(1, N + 1):
            if not flag and temp[r][c] == 1:
                if r == 1 or r == N:
                    break
                if temp[r - 1][c - 1] == 0 and temp[r - 1][c] == 0 and temp[r - 1][c + 1] == 0:
                    break
                elif temp[r + 1][c - 1] == 0 and temp[r + 1][c] == 0 and temp[r + 1][c + 1] == 0:
                    break
                flag = True
                continue
            if flag and temp[r][c] == 0:
                temp[r][c] = 1
                continue
            if flag and temp[r][c] == 1:
                flag = False
                break

    score = [0] * 5
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if 1 <= r < y + d1 and 1 <= c <= x:
                if temp[r][c] == 0:
                    score[0] += MAP[r][c]
            elif 1 <= r <= y + d2 and x < c <= N:
                if temp[r][c] == 0:
                    score[1] += MAP[r][c]
            elif y + d1 <= r <= N and 1 <= c < x - d1 + d2:
                if temp[r][c] == 0:
                    score[2] += MAP[r][c]
            elif y + d2 < r <= N and x - d1 + d2 <= c <= N:
                if temp[r][c] == 0:
                    score[3] += MAP[r][c]
    score[4] = SUM - (score[0] + score[1] + score[2] + score[3])
    diff = max(score) - min(score)
    min_diff = min(diff, min_diff)
print(min_diff)

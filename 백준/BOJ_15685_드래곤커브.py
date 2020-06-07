N = int(input())
MAP = [[0 for _ in range(101)] for _ in range(101)]
for i in range(N):
    x, y, d, g = map(int, input().split())
    S = [[y, x]]
    if d == 0: S.append([y, x + 1])
    elif d == 1: S.append([y - 1, x])
    elif d == 2: S.append([y, x - 1])
    else: S.append([y + 1, x])

    for j in range(g):
        baseline = S[-1]
        for k in range(len(S) - 2, -1, -1):
            dy = baseline[0] - S[k][0]
            dx = baseline[1] - S[k][1]
            S.append([baseline[0] - dx, baseline[1] + dy])
    for j in range(len(S)):
        MAP[S[j][0]][S[j][1]] = 1

count = 0
for i in range(100):
    for j in range(100):
        if MAP[i][j] == 1 and MAP[i][j + 1] == 1 and MAP[i + 1][j] == 1 and MAP[i + 1][j + 1] == 1:
            count += 1

print(count)
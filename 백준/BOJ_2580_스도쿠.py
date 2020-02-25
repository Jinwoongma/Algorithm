import sys

def dfs(index):
    if index == 81:
        for i in range(9):
            print(' '.join(map(str, data[i])))
        sys.exit(0)

    y = index // 9
    x = index % 9
    if data[y][x] == 0:
        for i in range(1, 10):
            if not rowCheck[y][i] and not colCheck[x][i] and not squareCheck[3 * (y // 3) + (x // 3)][i]:
                rowCheck[y][i] = True
                colCheck[x][i] = True
                squareCheck[3 * (y // 3) + (x // 3)][i] = True
                data[y][x] = i
                dfs(index + 1)
                rowCheck[y][i] = False
                colCheck[x][i] = False
                squareCheck[3 * (y // 3) + (x // 3)][i] = False
                data[y][x] = 0
    else:
        dfs(index + 1)


data = [list(map(int, input().split())) for _ in range(9)]
rowCheck = [[False for _ in range(10)] for _ in range(9)]
colCheck = [[False for _ in range(10)] for _ in range(9)]
squareCheck = [[False for _ in range(10)] for _ in range(9)]

for i in range(9):
    for j in range(9):
        if data[i][j] != 0:
            rowCheck[i][data[i][j]] = True
            colCheck[j][data[i][j]] = True
            squareCheck[3 * (i // 3) + (j // 3)][data[i][j]] = True

MAP = []
for i in range(9):
    MAP += data[i]
dfs(0)
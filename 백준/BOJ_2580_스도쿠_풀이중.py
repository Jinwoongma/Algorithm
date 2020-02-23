def search(y, x):
    row, col, square = [], [], []

    check = [False for _ in range(10)]
    for i in range(9):
        if MAP[y][i] != 0:
            check[MAP[y][i]] = True
    for i in range(1, 10):
        if not check[i]: row.append(i)

    check = [False for _ in range(10)]
    for i in range(9):
        if MAP[i][x] != 0:
            check[MAP[i][x]] = True
    for i in range(1, 10):
        if not check[i]: col.append(i)

    check = [False for _ in range(10)]
    for i in range((y // 3) * 3, (y // 3) * 3 + 3):
        for j in range((x // 3) * 3, (x // 3) * 3 + 3):
            if MAP[i][j] != 0:
                check[MAP[i][j]] = True
    for i in range(1, 10):
        if not check[i]: square.append(i)

    return row, col, square


def check():
    for i in range(9):
        for j in range(9):
            if MAP[i][j] == 0:
                return False
    return True


def same(num):
    if num in col and num in square:
        return True
    else: return False

MAP = [list(map(int, input().split())) for _ in range(9)]
while True:
    if check(): break
    for i in range(9):
        for j in range(9):
            if MAP[i][j] == 0:
                row, col, square = search(i, j)

                if len(row) == 1:
                    MAP[i][j] = row[0]
                    continue
                elif len(col) == 1:
                    MAP[i][j] = col[0]
                    continue
                elif len(square) == 1:
                    MAP[i][j] = square[0]
                    continue
                else:
                    for k in range(len(row)):
                        if same(row[k]):
                            MAP[i][j] = row[k]
                            break


for i in range(9):
    print(' '.join(map(str, MAP[i])))
print()

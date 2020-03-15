def cut(y, x):
    arr = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(y, y + 8):
        for j in range(x, x + 8):
            arr[i - y][j - x] = MAP[i][j]
    return arr


R, C = map(int, input().split())
MAP = [list(map(str, input().strip())) for _ in range(R)]
result = 0xfffff

for i in range(R - 8 + 1):
    for j in range(C - 8 + 1):
        new_MAP = cut(i, j)
        cnt1, cnt2 = 0, 0
        for r in range(8):
            for c in range(8):
                if r % 2 == 0:
                    if c % 2 == 0 and new_MAP[r][c] == 'B':
                        cnt1 += 1
                    elif c % 2 == 1 and new_MAP[r][c] == 'W':
                        cnt1 += 1
                    elif c % 2 == 0 and new_MAP[r][c] == 'W':
                        cnt2 += 1
                    elif c % 2 == 1 and new_MAP[r][c] == 'B':
                        cnt2 += 1

                elif r % 2 == 1:
                    if c % 2 == 0 and new_MAP[r][c] == 'W':
                        cnt1 += 1
                    elif c % 2 == 1 and new_MAP[r][c] == 'B':
                        cnt1 += 1
                    elif c % 2 == 0 and new_MAP[r][c] == 'B':
                        cnt2 += 1
                    elif c % 2 == 1 and new_MAP[r][c] == 'W':
                        cnt2 += 1

        result = min(result, min(cnt1, cnt2))

print(result)

def adjust(y, x, length):
    for r in range(y, y + length + 1):
        for c in range(x, x + length + 1):
            if c >= 10 or r >= 10: return False
            if MAP[r][c] == 0: return False
    return True


def change(y, x, length):
    for r in range(y, y + length + 1):
        for c in range(x, x + length + 1):
            if MAP[r][c] == 1: MAP[r][c] = 0


def repair(y, x, length):
    for r in range(y, y + length + 1):
        for c in range(x, x + length + 1):
            if MAP[r][c] == 0: MAP[r][c] = 1


def dfs(y, x):
    global min_result
    if x == 10:
        dfs(y + 1, 0)
        return
    if y == 10:
        min_result = min(min_result, 25 - sum(remain))
        return
    if MAP[y][x] == 0:
        dfs(y, x + 1)
        return
    else:
        for i in range(5):
            if adjust(y, x, i) and remain[i] > 0:
                change(y, x, i)
                remain[i] -= 1

                dfs(y, x)

                repair(y, x, i)
                remain[i] += 1
            else: continue

MAP = [list(map(int, input().split())) for _ in range(10)]
remain = [5, 5, 5, 5, 5]
min_result = 0xffffffff

dfs(0, 0)
if min_result == 0xffffffff: print(-1)
else: print(min_result)

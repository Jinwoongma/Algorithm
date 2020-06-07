def isPossible(y, x, l):
    for i in range(y, y + l + 1):
        for j in range(x, x + l + 1):
            if i >= 10 or j >= 10 or MAP[i][j] == 0 :
                return False
    return True


def change(y, x, l, v):
    for i in range(y, y + l + 1):
        for j in range(x, x + l + 1):
            MAP[i][j] = v
    return


def solve(y, x, cnt):
    global answer
    if x == 10:
        y += 1
        x = 0
    if y == 10:
        answer = min(answer, cnt)
        return

    if MAP[y][x] == 0:
        solve(y, x + 1, cnt)
    elif MAP[y][x] == 1:
        for i in range(5):
            if isPossible(y, x, i) and remain[i] > 0:
                change(y, x, i, 0)
                remain[i] -= 1
                solve(y, x + 1, cnt + 1)
                change(y, x, i, 1)
                remain[i] += 1


MAP = [list(map(int, input().split())) for _ in range(10)]
remain = [5, 5, 5, 5, 5]
answer = 0xffffff
solve(0, 0, 0)

print(-1 if answer == 0xffffff else answer)
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

def check(MAP):
    for i in range(10):
        for j in range(10):
            if MAP[i][j] != 0:
                return False
    return True


MAP = [list(map(int, input().split())) for _ in range(10)]
remain = [5, 5, 5, 5, 5]
count = 0
flag = True

for i in range(4, -1, -1):
    for r in range(10):
        if not flag: break
        for c in range(10):
            if MAP[r][c] == 1:
                if not adjust(r, c, i): continue
                else:
                    if remain[i] == 0:
                        continue
                    else:
                        change(r, c, i)
                        remain[i] -= 1
                        count += 1
                        continue

if check(MAP): print(count)
else: print(-1)

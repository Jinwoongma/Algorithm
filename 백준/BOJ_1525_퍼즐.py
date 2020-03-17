from _collections import deque

MAP = [list(map(int, input().split())) for _ in range(3)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
result = 0xfffff

new_MAP = ''
for i in range(3):
    new_MAP += ''.join(map(str, MAP[i]))
    for j in range(3):
        if MAP[i][j] == 0:
            sy, sx = i, j

check = set()
Q = deque()
Q.append([sy, sx, 0, new_MAP])
check.add(new_MAP)

while Q:
    y, x, cnt, str_MAP = Q.popleft()
    if str_MAP == '123456780':
        result = cnt
        break

    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= 3 or tx < 0 or tx >= 3: continue
        lst_MAP = list(map(str, str_MAP.strip()))
        lst_MAP[y * 3 + x], lst_MAP[ty * 3 + tx] = lst_MAP[ty * 3 + tx], lst_MAP[y * 3 + x]
        new_str_MAP = ''.join(map(str, lst_MAP))
        if new_str_MAP not in check:
            check.add(new_str_MAP)
            Q.append([ty, tx, cnt + 1, new_str_MAP])

if result == 0xfffff:
    print(-1)
else:
    print(result)
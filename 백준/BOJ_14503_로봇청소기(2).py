# 23:20 ~ 12:00
def turn_left(d):
    if d == 0: return 3
    elif d == 1: return 0
    elif d == 2: return 1
    elif d == 3: return 2


R, C = map(int, input().split())
y, x, d = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
dy = [-1, 0, 1, 0]; dx = [0, 1, 0, -1]  # 북 동 남 서
ans = 1
MAP[y][x] = '.'

while True:
    for i in range(4):
        d = turn_left(d)
        ty, tx = y + dy[d], x + dx[d]
        if MAP[ty][tx] == 0:
            y, x = ty, tx
            ans += 1
            MAP[y][x] = '.'
            break
    else:
        ty, tx = y - dy[d], x - dx[d]
        if MAP[ty][tx] == 0:
            y, x = ty, tx
        else:
            if MAP[ty][tx] == 1:
                break
            else:
                y, x = ty, tx
print(ans)
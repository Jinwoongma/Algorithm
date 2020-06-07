def get_distance(y, x, d):
    ret = 0
    flag = True
    ty, tx = y, x
    while True:
        ty += dy[d]
        tx += dx[d]
        if ty < 0 or ty >= N or tx < 0 or tx >= N: break
        if MAP[ty][tx] != 0:
            flag = False
            break
        else: ret += 1
    if not flag: return -1
    else: return ret


def change(y, x, d, l, v):
    ty, tx = y, x
    for i in range(1, l + 1):
        ty += dy[d]
        tx += dx[d]
        MAP[ty][tx] = v


def solve(y, x, check, cnt, tot):
    global answer, max_connect
    if (total_core - check + cnt) < max_connect:
        return
    if x == N:
        y += 1
        x = 0
    if y == N:
        if cnt > max_connect:
            max_connect = cnt
            answer = tot
        elif cnt == max_connect:
            answer = min(answer, tot)
        return

    if MAP[y][x] == 1:
        for dir in range(4):
            dist = get_distance(y, x, dir)
            if dist == -1:
                solve(y, x + 1, check + 1, cnt, tot)
                continue
            else:
                change(y, x, dir, dist, 2)
                solve(y, x + 1, check + 1, cnt + 1, tot + dist)
                change(y, x, dir, dist, 0)

    else:
        solve(y, x + 1, check, cnt, tot)


TC = int(input())
for tc in range(TC):
    N = int(input())
    total_core = 0
    MAP = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 1:
                total_core += 1
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    answer = 0
    max_connect = 0
    solve(0, 0, 0, 0, 0)
    print('#{} {}'.format(tc + 1, answer))
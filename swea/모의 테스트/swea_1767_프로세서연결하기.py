def install(y, x, dir):
    ty, tx = y, x
    while True:
        ty += dy[dir]
        tx += dx[dir]
        if ty < 0 or ty >= N or tx < 0 or tx >= N: break
        if MAP[ty][tx] != 0:
            if MAP[ty][tx] == 1: continue
            else: break
        else:
            MAP[ty][tx] = 2


def uninstall(y, x, dir):
    ty, tx = y, x
    while True:
        ty += dy[dir]
        tx += dx[dir]
        if ty < 0 or ty >= N or tx < 0 or tx >= N: break
        if MAP[ty][tx] == 2:
            MAP[ty][tx] = 0


def isPossible(y, x, dir):
    ty, tx = y, x
    while True:
        ty += dy[dir]
        tx += dx[dir]
        if ty < 0 or ty >= N or tx < 0 or tx >= N: break
        if MAP[ty][tx] != 0: return False
    return True


def dfs(index):
    global count
    global min_line
    global max_count

    if L - index + count < max_count: return

    if index == L:
        if count > max_count:
            max_count = count
            min_line = 0xffffffff
            line_count = 0
            for i in range(N):
                for j in range(N):
                    if MAP[i][j] == 2:
                        line_count += 1
            if line_count < min_line:
                min_line = line_count

        elif count == max_count:
            max_count = count
            line = 0
            for i in range(N):
                for j in range(N):
                    if MAP[i][j] == 2:
                        line += 1
            if line < min_line:
                min_line = line
        return
    else:
        for dir in range(4):
            if isPossible(core[index][0], core[index][1], dir):
                count += 1
                install(core[index][0], core[index][1], dir)
                dfs(index + 1)
                uninstall(core[index][0], core[index][1], dir)
                count -= 1
            else:
                dfs(index + 1)


TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    dy = [1, -1, 0, 0]; dx = [0, 0, -1, 1]
    core = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 1: core.append([i, j])
    L = len(core)

    count, max_count = 0, -1
    line, min_line = 0, 0xffffffff
    dfs(0)
    print('#{} {}'.format(tc + 1, min_line))
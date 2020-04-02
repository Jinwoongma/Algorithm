from _collections import deque
TC = int(input())
for tc in range(TC):
    R, C = map(int, input().split())
    MAP = [list(map(str, input().strip())) for _ in range(R)]
    visited = [[[[False for _ in range(16)] for _ in range(4)] for _ in range(C)] for _ in range(R)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    #  visited[y][x][dir][mem]

    Q = deque()
    Q.append([0, -1, 3, 0])
    ans = False
    while Q:
        y, x, dir, mem = Q.popleft()
        ty, tx = y + dy[dir], x + dx[dir]

        if ty >= R: ty = 0
        if ty < 0: ty = R - 1
        if tx >= C: tx = 0
        if tx < 0: tx = C - 1

        if MAP[ty][tx] == '>':
            dir = 3
        elif MAP[ty][tx] == '<':
            dir = 2
        elif MAP[ty][tx] == '^':
            dir = 0
        elif MAP[ty][tx] == 'v':
            dir = 1
        elif MAP[ty][tx] == '_':
            if mem == 0:
                dir = 3
            else:
                dir = 2
        elif MAP[ty][tx] == '|':
            if mem == 0:
                dir = 1
            else:
                dir = 0
        elif MAP[ty][tx] == '?':
            for tdir in range(4):
                if not visited[ty][tx][tdir][mem]:
                    visited[ty][tx][tdir][mem] = True
                    Q.append([ty, tx, tdir, mem])
            continue
        elif MAP[ty][tx] == '@':
            ans = True
            break
        elif MAP[ty][tx] in '0123456789':
            mem = int(MAP[ty][tx])
        elif MAP[ty][tx] == '+':
            if mem == 15:
                mem = 0
            else:
                mem += 1
        elif MAP[ty][tx] == '-':
            if mem == 0:
                mem = 15
            else:
                mem -= 1

        if not visited[ty][tx][dir][mem]:
            visited[ty][tx][dir][mem] = True
            Q.append([ty, tx, dir, mem])

    if not ans:
        print('#{} NO'.format(tc + 1))
    else:
        print('# YES'.format(tc + 1))
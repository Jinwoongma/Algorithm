TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    result = []

    for r in range(N):
        for c in range(N):
            if MAP[r][c] != 0 and not visited[r][c]:
                ty, tx = r, c
                area, sero = 0, 0
                while True:
                    if tx == c and MAP[ty][tx] == 0: break
                    if tx >= N or MAP[ty][tx] == 0:
                        ty += 1
                        tx = c
                        sero += 1
                        continue
                    else:
                        visited[ty][tx] = True
                        area += 1
                        tx += 1
                result.append([area, sero, area//sero])
    result = sorted(result, key=lambda x:(x[0], x[1]))

    print('#{} {}'.format(tc + 1, len(result)), end='')
    for i in range(len(result)):
        print(' {} {}'.format(result[i][1], result[i][2]), end='')
    print()
from _collections import deque
import sys
sys.stdin = open('input.txt', 'r')

TC = int(input())
for tc in range(TC):
    R, C, sy, sx, L = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(R)]
    visited = [[0 for _ in range(C)] for _ in range(R)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    Q = deque()
    day = 1
    Q.append([sy, sx, day])
    visited[sy][sx] = 1
    flag = False

    while Q:
        y, x, day = Q.popleft()
        if day == L:
            cnt = 0
            for r in range(R):
                for c in range(C):
                    if visited[r][c]:
                        cnt += 1
            print('#{} {}'.format(tc + 1, cnt))
            flag = True
            break

        if MAP[y][x] == 1:
            if y - 1 >= 0:
                if not visited[y - 1][x] and MAP[y - 1][x] != 0:
                    if MAP[y - 1][x] == 1 or MAP[y - 1][x] == 2 or MAP[y - 1][x] == 5 or MAP[y - 1][x] == 6:
                        visited[y - 1][x] = 1
                        Q.append([y - 1, x, day + 1])
            if y + 1 < R:
                if not visited[y + 1][x] and MAP[y + 1][x] != 0:
                    if MAP[y + 1][x] == 1 or MAP[y + 1][x] == 2 or MAP[y + 1][x] == 4 or MAP[y + 1][x] == 7:
                        visited[y + 1][x] = 1
                        Q.append([y + 1, x, day + 1])
            if x - 1 >= 0:
                if not visited[y][x - 1] and MAP[y][x - 1] != 0:
                    if MAP[y][x - 1] == 1 or MAP[y][x - 1] == 3 or MAP[y][x - 1] == 4 or MAP[y][x - 1] == 5:
                        visited[y][x - 1] = 1
                        Q.append([y, x - 1, day + 1])
            if x + 1 < C:
                if not visited[y][x + 1] and MAP[y][x + 1] != 0:
                    if MAP[y][x + 1] == 1 or MAP[y][x + 1] == 3 or MAP[y][x + 1] == 6 or MAP[y][x + 1] == 7:
                        visited[y][x + 1] = 1
                        Q.append([y, x + 1, day + 1])

        elif MAP[y][x] == 2:
            if y - 1 >= 0:
                if not visited[y - 1][x] and MAP[y - 1][x] != 0:
                    if MAP[y - 1][x] == 1 or MAP[y - 1][x] == 2 or MAP[y - 1][x] == 5 or MAP[y - 1][x] == 6:
                        visited[y - 1][x] = 1
                        Q.append([y - 1, x, day + 1])
            if y + 1 < R:
                if not visited[y + 1][x] and MAP[y + 1][x] != 0:
                    if MAP[y + 1][x] == 1 or MAP[y + 1][x] == 2 or MAP[y + 1][x] == 4 or MAP[y + 1][x] == 7:
                        visited[y + 1][x] = 1
                        Q.append([y + 1, x, day + 1])

        elif MAP[y][x] == 3:
            if x - 1 >= 0:
                if not visited[y][x - 1] and MAP[y][x - 1] != 0:
                    if MAP[y][x - 1] == 1 or MAP[y][x - 1] == 3 or MAP[y][x - 1] == 4 or MAP[y][x - 1] == 5:
                        visited[y][x - 1] = 1
                        Q.append([y, x - 1, day + 1])
            if x + 1 < C:
                if not visited[y][x + 1] and MAP[y][x + 1] != 0:
                    if MAP[y][x + 1] == 1 or MAP[y][x + 1] == 3 or MAP[y][x + 1] == 6 or MAP[y][x + 1] == 7:
                        visited[y][x + 1] = 1
                        Q.append([y, x + 1, day + 1])

        elif MAP[y][x] == 4:
            if y - 1 >= 0:
                if not visited[y - 1][x] and MAP[y - 1][x] != 0:
                    if MAP[y - 1][x] == 1 or MAP[y - 1][x] == 2 or MAP[y - 1][x] == 5 or MAP[y - 1][x] == 6:
                        visited[y - 1][x] = 1
                        Q.append([y - 1, x, day + 1])
            if x + 1 < C:
                if not visited[y][x + 1] and MAP[y][x + 1] != 0:
                    if MAP[y][x + 1] == 1 or MAP[y][x + 1] == 3 or MAP[y][x + 1] == 6 or MAP[y][x + 1] == 7:
                        visited[y][x + 1] = 1
                        Q.append([y, x + 1, day + 1])

        elif MAP[y][x] == 5:
            if y + 1 < R:
                if not visited[y + 1][x] and MAP[y + 1][x] != 0:
                    if MAP[y + 1][x] == 1 or MAP[y + 1][x] == 2 or MAP[y + 1][x] == 4 or MAP[y + 1][x] == 7:
                        visited[y + 1][x] = 1
                        Q.append([y + 1, x, day + 1])
            if x + 1 < C:
                if not visited[y][x + 1] and MAP[y][x + 1] != 0:
                    if MAP[y][x + 1] == 1 or MAP[y][x + 1] == 3 or MAP[y][x + 1] == 6 or MAP[y][x + 1] == 7:
                        visited[y][x + 1] = 1
                        Q.append([y, x + 1, day + 1])

        elif MAP[y][x] == 6:
            if y + 1 < R:
                if not visited[y + 1][x] and MAP[y + 1][x] != 0:
                    if MAP[y + 1][x] == 1 or MAP[y + 1][x] == 2 or MAP[y + 1][x] == 4 or MAP[y + 1][x] == 7:
                        visited[y + 1][x] = 1
                        Q.append([y + 1, x, day + 1])
            if x - 1 >= 0:
                if not visited[y][x - 1] and MAP[y][x - 1] != 0:
                    if MAP[y][x - 1] == 1 or MAP[y][x - 1] == 3 or MAP[y][x - 1] == 4 or MAP[y][x - 1] == 5:
                        visited[y][x - 1] = 1
                        Q.append([y, x - 1, day + 1])

        elif MAP[y][x] == 7:
            if y - 1 >= 0:
                if not visited[y - 1][x] and MAP[y - 1][x] != 0:
                    if MAP[y - 1][x] == 1 or MAP[y - 1][x] == 2 or MAP[y - 1][x] == 5 or MAP[y - 1][x] == 6:
                        visited[y - 1][x] = 1
                        Q.append([y - 1, x, day + 1])
            if x - 1 >= 0:
                if not visited[y][x - 1] and MAP[y][x - 1] != 0:
                    if MAP[y][x - 1] == 1 or MAP[y][x - 1] == 3 or MAP[y][x - 1] == 4 or MAP[y][x - 1] == 5:
                        visited[y][x - 1] = 1
                        Q.append([y, x - 1, day + 1])

    if not flag:
        cnt = 0
        for r in range(R):
            for c in range(C):
                if visited[r][c]:
                    cnt += 1
        print('#{} {}'.format(tc + 1, cnt))

import sys
sys.stdin = open('input_1226.txt', 'r')
from collections import deque

def bfs(y, x):
    global ans
    Q = deque()
    visited[y][x] = True
    Q.append([y, x])

    while Q:
        s = Q.popleft()
        for dir in range(4):
            ty, tx = s[0] + dy[dir], s[1] + dx[dir]
            if 0 <= ty < 16 and 0 <= tx < 16:
                if MAP[ty][tx] == '3':
                    ans = 1
                    break
                elif not visited[ty][tx] and MAP[ty][tx] != '1':
                    Q.append([ty, tx])
                    visited[ty][tx] = True

for tc in range(1, 11):
    t = int(input())
    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    MAP = [str(input()) for _ in range(16)]
    visited = [[False for _ in range(16)] for _ in range(16)]

    ans = 0
    for i in range(16):
        for j in range(16):
            if MAP[i][j] == '2':
                s_y, s_x = i, j

    bfs(s_y, s_x)
    print('#{} {}'.format(tc, ans))
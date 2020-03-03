import sys
sys.stdin = open('input.txt', 'r')
from _collections import deque

def bfs(y, x):
    global cnt
    Q = deque()
    Q.append([y, x])
    while Q:
        y, x = Q.popleft()
        for dir in range(4):
            ty = y + dy[dir]
            tx = x + dx[dir]
            if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
            if MAP[ty][tx] - MAP[y][x] == 1:
                Q.append([ty, tx])
                cnt += 1


TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    max_cnt = -1
    max_idx = -1

    for r in range(N):
        for c in range(N):
            cnt = 1
            bfs(r, c)
            if cnt > max_cnt:
                max_cnt = cnt
                max_idx = MAP[r][c]
            if cnt == max_cnt:
                max_idx = min(max_idx, MAP[r][c])

    print('#{} {} {}'.format(tc + 1, max_idx, max_cnt))
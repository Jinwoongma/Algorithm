import sys
from _collections import deque
sys.stdin = open('input.txt', 'r')

def bfs(y, x, k):
    global result
    Q = deque()
    Q.append([y, x, k])
    while Q:
        y, x, k = Q.popleft()
        result = max(result, len(k))
        for dir in range(4):
            ty, tx, tk = y + dy[dir], x + dx[dir], k
            if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
            if MAP[ty][tx] not in k:
                tk += MAP[ty][tx]
                Q.append([ty, tx, tk])


TC = int(input())
for tc in range(TC):
    R, C = map(int, input().split())
    MAP = [list(map(str, input().strip())) for _ in range(R)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    result = -1
    k = MAP[0][0]
    bfs(0, 0, k)
    print('#{} {}'.format(tc + 1, result))
from _collections import deque
import sys

r, c = map(int, sys.stdin.readline().split())
MAP = [str(sys.stdin.readline()) for _ in range(r)]
wall = []
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
min_length = 0xffffffff

visited = [[[0 for _ in range(2)] for _ in range(c)] for _ in range(r)]
Q = deque()
Q.append([0, 0, 1, 0])
visited[0][0][0] = True

while Q:
    s = Q.popleft()
    y, x, l, p= s[0], s[1], s[2], s[3]
    if y == r - 1 and x == c - 1:
        min_length = min(min_length, l)
        break
    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= r or tx < 0 or tx >= c: continue

        if MAP[ty][tx] == '1' and p == 0:
            visited[ty][tx][1] = True
            Q.append([ty, tx, l + 1, p + 1])

        elif MAP[ty][tx] == '0' and not visited[ty][tx][p]:
            visited[ty][tx][p] = True
            Q.append([ty, tx, l + 1, p])


if min_length == 0xffffffff:
    print(-1)
else: print(min_length)
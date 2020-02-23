from _collections import deque
from copy import deepcopy

r, c = map(int, input().split())
MAP = [list(map(str, input().strip())) for _ in range(r)]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
day = 0
Q = deque()
temp = []
for i in range(r):
    for j in range(c):
        if MAP[i][j] != '.' and MAP[i][j] != '9':
            temp.append([i, j])
Q.append([temp, 0, []])

while Q:
    s, day, past_ADD = Q.popleft()
    DEL = []
    ADD = []

    for i in range(len(s)):
        y, x = s[i][0], s[i][1]
        cnt = 0
        for dir in range(8):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
            if MAP[ty][tx] == '.': cnt += 1
            if cnt >= int(MAP[y][x]):
                DEL.append([y, x])
                break
        else: ADD.append([y, x])

    if len(DEL) != 0:
        for j in range(len(DEL)):
            MAP[DEL[j][0]][DEL[j][1]] = '.'

    if past_ADD == ADD:
        print(day)
        break

    Q.append([ADD, day + 1, ADD])
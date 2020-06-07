# 19:57 ~ 20:16
from _collections import deque

def turn(cur, dir):
    if dir == 'L':
        if cur == 0: return 2
        elif cur == 1: return 3
        elif cur == 2: return 1
        else: return 0
    elif dir == 'D':
        if cur == 0: return 3
        elif cur == 1: return 2
        elif cur == 2: return 0
        else: return 1


N = int(input())
K = int(input())
MAP = [[0 for _ in range(N)] for _ in range(N)]
bam = deque()  # [(y1, x1), (y2, x2)...] << tail
bam.append([0, 0])
time = [0] * 10010
dy = [0, 0, -1, 1]; dx = [1, -1, 0, 0]  # 오 왼 위 아래

for i in range(K):
    y, x = map(int, input().split())
    MAP[y - 1][x - 1] = 1

L = int(input())
for i in range(L):
    t, d = map(str, input().split())
    time[int(t)] = d

t, y, x, d = 1, 0, 0, 0
while True:
    ty, tx = y + dy[d], x + dx[d]
    if ty < 0 or ty >= N or tx < 0 or tx >= N: break
    if [ty, tx] in bam: break
    bam.appendleft([ty, tx])
    if MAP[ty][tx] == 1:
        MAP[ty][tx] = 0
    else:
        bam.pop()

    if time[t] != 0:
        d = turn(d, time[t])
    y, x = ty, tx
    t += 1
print(t)
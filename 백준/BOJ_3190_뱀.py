from _collections import deque

def turn(cur, dir):
    if dir == 'L':
        if cur == 0: return 2
        elif cur == 1: return 3
        elif cur == 2: return 1
        elif cur == 3: return 0
    elif dir == 'D':
        if cur == 0 : return 3
        elif cur == 1: return 2
        elif cur == 2: return 0
        elif cur == 3: return 1


N = int(input())
MAP = [[0 for _ in range(N)] for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
K = int(input())
for i in range(K):
    y, x = map(int, input().split())
    MAP[y - 1][x - 1] = 1
MAP[0][0] = 2

L = int(input())
time = [0] * 100001
for i in range(L):
    t, move = input().split()
    time[int(t)] = move

Q = deque()
Q.append([0, 0])
dir, t = 3, 0

while True:
    y, x = Q[-1][0], Q[-1][1]
    if time[t] != 0:
        dir = turn(dir, time[t])
    ty, tx = y + dy[dir], x + dx[dir]

    if ty < 0 or ty >= N or tx < 0 or tx >= N:
        print(t + 1)
        break

    if [ty, tx] in Q:
        print(t + 1)
        break

    if MAP[ty][tx] == 1:  # 이동한 지역이 사과일 경우 (길이 증가)
        MAP[ty][tx] = 2
        Q.append([ty, tx])

    else:  # 이동한 지역이 사과가 아닐 경우 (길이 증가 후 꼬리 감소)
        MAP[ty][tx] = 2
        Q.append([ty, tx])
        Q.popleft()

    t += 1
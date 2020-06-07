import sys

def turnLeft(dir):
    if dir == 'W': return 'S'
    if dir == 'S': return 'E'
    if dir == 'E': return 'N'
    if dir == 'N': return 'W'


def turnRight(dir):
    if dir == 'W': return 'N'
    if dir == 'N': return 'E'
    if dir == 'E': return 'S'
    if dir == 'S': return 'W'


C, R = map(int, input().split())
N, M = map(int, input().split())
loc = [0 for _ in range(N + 1)]
dir = {'N': (1, 0), 'S': (-1, 0), 'W': (0, -1), 'E': (0, 1)}

for i in range(N):
    x, y, d = map(str, input().split())
    loc[i + 1] = [int(y), int(x), d]

for i in range(M):
    num, code, rep = map(str, input().split())
    num, rep = int(num), int(rep)
    y, x, d = loc[num]
    if code == 'F':
        ty, tx, l = y, x, 0
        while True:
            if l == rep: break
            ty, tx = ty + dir[d][0], tx + dir[d][1]
            if ty <= 0 or ty > R or tx <= 0 or tx > C:
                print('Robot {} crashes into the wall'.format(num))
                sys.exit(0)
            for j in range(1, N + 1):
                if j == num: continue
                if ty == loc[j][0] and tx == loc[j][1]:
                    print('Robot {} crashes into robot {}'.format(num, j))
                    sys.exit(0)
            l += 1
        loc[num][0], loc[num][1] = ty, tx

    elif code == 'L':
        rep = rep % 4
        for j in range(rep):
            d = turnLeft(d)
        loc[num][2] = d

    elif code == 'R':
        rep = rep % 4
        for j in range(rep):
            d = turnRight(d)
        loc[num][2] = d

print('OK')

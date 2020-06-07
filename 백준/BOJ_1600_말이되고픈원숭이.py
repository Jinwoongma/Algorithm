from _collections import deque

def bfs(y, x, K, day):
    global flag

    Q = deque()
    Q.append([y, x, K, day])
    visited[y][x][K] = True
    while Q:
        y, x, k, day = Q.popleft()
        if y == r - 1 and x == c - 1:
            print(day)
            flag = True
            break
        if k > 0:
            for dir in range(8):
                ty = y + kdy[dir]
                tx = x + kdx[dir]
                if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
                if MAP[ty][tx] == 0 and not visited[ty][tx][k - 1]:
                    visited[ty][tx][k - 1] = True
                    Q.append([ty, tx, k - 1, day + 1])

            for dir in range(4):
                ty = y + dy[dir]
                tx = x + dx[dir]
                if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
                if MAP[ty][tx] == 0 and not visited[ty][tx][k]:
                    visited[ty][tx][k] = True
                    Q.append([ty, tx, k, day + 1])

        else:
            for dir in range(4):
                ty = y + dy[dir]
                tx = x + dx[dir]
                if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
                if MAP[ty][tx] == 0 and not visited[ty][tx][k]:
                    visited[ty][tx][k] = True
                    Q.append([ty, tx, k, day + 1])



K = int(input())
c, r = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(r)]
visited = [[[False for _ in range(K + 1)] for _ in range(c)] for _ in range(r)]
kdy = [2, 1, -1, -2, -2, -1, 1, 2]
kdx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
flag = False

bfs(0, 0, K, 0)
if not flag: print(-1)
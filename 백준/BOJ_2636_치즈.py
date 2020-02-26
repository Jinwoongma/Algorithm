from _collections import deque

def bfs(y, x):
    Q = deque()
    Q.append([y, x])
    visited[y][x] = True
    while Q:
        y, x = Q.popleft()
        for dir in range(4):
            ty = y + dy[dir]
            tx = x + dx[dir]
            if ty < 0 or ty >= r or tx < 0 or tx >= c: continue

            if MAP[ty][tx] == 1:
                erase.append([ty, tx])

            if MAP[ty][tx] == 0:
                if not visited[ty][tx]:
                    visited[ty][tx] = True
                    Q.append([ty, tx])


def check():
    count = 0
    for i in range(r):
        for j in range(c):
            if MAP[i][j] == 1:
                count += 1
    return count


r, c = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(r)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
year = 1
remain = 0xffffffff
while True:
    erase = []
    visited = [[False for _ in range(c)] for _ in range(r)]
    before = remain
    remain = check()
    if remain > 0:
        bfs(0, 0)
        for i in range(len(erase)):
            if MAP[erase[i][0]][erase[i][1]] > 0:
                MAP[erase[i][0]][erase[i][1]] -= 1
        year += 1
    else:
        print(year - 1)
        print(before)
        break

from collections import deque

col, row = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(row)]
visited = [[False for _ in range(col)] for _ in range(row)]
D = [[0 for _ in range(col)] for _ in range(row)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
Q = deque()

def is_range(y, x):
    if x >= 0 and x < col and y >= 0 and y < row:
        return True
    else:
        return False

def is_nozero(data):
    zero_count = 0
    for r in range(row):
        for c in range(col):
            if data[r][c] == 0:
                zero_count += 1
    if zero_count == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    for r in range(row):
        for c in range(col):
            if data[r][c] == 1:
                Q.append((r, c))

    while len(Q) != 0:
        loop_size = len(Q)
        for i in range(loop_size):
            v = Q.popleft()
            y, x = v[0], v[1]
            for dir in range(4):
                ty, tx = y + dy[dir], x + dx[dir]
                if is_range(ty, tx):
                    if not visited[ty][tx] and data[ty][tx] == 0:
                        D[ty][tx] = D[y][x] + 1
                        visited[ty][tx] = True
                        Q.append((ty, tx))

    max_day = -1
    flag = True
    for r in range(row):
        if not flag:
            break
        for c in range(col):
            if not (r == row - 1 and c == col - 1):
                if D[r][c] == 0 and data[r][c] == 0:
                    print(-1)
                    flag = False
                    break
            if D[r][c] >= max_day:
                max_day = D[r][c]

    if max_day >= 0:
        print(max_day)

    elif is_nozero(data):
        print(0)


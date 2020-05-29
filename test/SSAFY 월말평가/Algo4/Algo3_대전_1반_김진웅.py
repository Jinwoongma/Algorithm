from _collections import deque


def cal_distance(start, end):
    sy, sx, ey, ex = start[0], start[1], end[0], end[1]
    visited = [[False for _ in range(N)] for _ in range(N)]
    Q = deque()
    Q.append([sy, sx, 0])
    visited[sy][sx] = True
    while Q:
        y, x, d = Q.popleft()
        if y == ey and x == ex:
            distance = d
            break
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
            if not visited[ty][tx] and A[ty][tx] != 1:
                Q.append([ty, tx, d + 1])
                visited[ty][tx] = True

    if distance % 2:
        distance = distance // 2 + 1
    else:
        distance = distance // 2
    return distance

def pick(index, now):
    global answer
    if index == 2:
        start, end = arr[0], arr[1]
        answer = min(answer, cal_distance(arr[0], arr[1]))
        return
    for i in range(now, n):
        if not check[i]:
            arr.append(starts[i])
            check[i] = True
            pick(index + 1, i)
            check[i] = False
            arr.pop()


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

starts = []
for i in range(N):
    for j in range(N):
        if A[i][j] == 2:
            starts.append((i, j))

n = len(starts)
check = [False for _ in range(n)]
arr = []
answer = 0xfffff
pick(0, 0)

print(answer)
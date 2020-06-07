from collections import deque


def bfs(arr):
    Q = deque()
    for i in birus:
        Q.append(i)
    while Q:
        y, x = Q.popleft()
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
            if arr[ty][tx] == 0:
                arr[ty][tx] = 2
                Q.append([ty, tx])
    ret = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 0:
                ret += 1
    return ret


def makeNew(arr):
    global answer
    new_arr = [[0 for _ in range(C)]for _ in range(R)]
    for i in range(R):
        for j in range(C):
            new_arr[i][j] = MAP[i][j]
    for idx in arr:
        y, x = idx // C, idx % C
        new_arr[y][x] = 1
    answer = max(answer, bfs(new_arr))


def Solve(index, start, N):
    if len(arr) == 3:
        makeNew(arr)
        return
    for i in range(start, N):
        if not visited[empty[i]]:
            visited[empty[i]] = True
            arr.append(empty[i])
            Solve(index + 1, i, N)
            arr.pop()
            visited[empty[i]] = False


R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
visited = [False for _ in range(64)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
empty, birus = [], []

for i in range(R):
    for j in range(C):
        if MAP[i][j] == 0:
            empty.append(i * C + j)
        elif MAP[i][j] == 2:
            birus.append([i, j])

arr = []
answer = -1
Solve(0, 0, len(empty))
print(answer)
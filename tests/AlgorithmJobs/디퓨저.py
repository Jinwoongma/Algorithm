from _collections import deque

def bfs(arr):
    global answer
    Q = deque()
    visited = [[False for _ in range(C)] for _ in range(R)]
    t = 0
    for i in range(len(arr)):
        y, x, t = D[arr[i]][0], D[arr[i]][1], 0
        Q.append([y, x, t])
        visited[y][x] = True

    while Q:
        y, x, t = Q.popleft()
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
            if not visited[ty][tx] and MAP[ty][tx] != 1:
                visited[ty][tx] = True
                Q.append([ty, tx, t + 1])

        flag = True
        for i in range(R):
            for j in range(C):
                if MAP[i][j] == 0 and not visited[i][j]:
                    flag = False
        if flag:
            answer = min(answer, t)
            break



def select(index, start):
    if index == N:
        # print(arr)
        bfs(arr)
        # print(aswer)
        return
    for i in range(start, L):
        if not check[i]:
            check[i] = True
            arr.append(i)
            select(index + 1, i)
            arr.pop()
            check[i] = False


TC = int(input())
for tc in range(TC):
    R, C, N = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(R)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    D = []
    flag = True
    for i in range(R):
        for j in range(C):
            if MAP[i][j] == 0:
                flag = False
            if MAP[i][j] == 2:
                D.append([i, j])

    if flag:
        print('#{} {}'.format(tc + 1, 0))
    else:
        answer = 0xfffff
        L = len(D)
        check = [False for _ in range(L)]
        arr = []
        select(0, 0)
        if answer == 0xfffff:
            print('#{} {}'.format(tc + 1, -1))
        else:
            print('#{} {}'.format(tc + 1, answer + 1))
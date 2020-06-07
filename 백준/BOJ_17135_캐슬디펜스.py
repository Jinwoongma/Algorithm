from _collections import deque
from copy import deepcopy

def combi(index, start):
    global max_kill
    if index == 3:
        new_MAP = deepcopy(MAP)
        ans = game(arr, new_MAP)
        max_kill = max(ans, max_kill)
        return
    for i in range(start, C):
        if not check[i]:
            check[i] = True
            arr.append(i)
            combi(index + 1, i)
            check[i] = False
            arr.pop()


def isNoEnemy(M):
    for i in range(R):
        for j in range(C):
            if M[i][j] == 1:
                return False
    return True


def move(M):
    for i in range(R - 1, -1, -1):
        for j in range(C):
            if M[i][j] == 1:
                if M[i + 1][j] == 2:
                    M[i][j] = 0
                elif M[i + 1][j] == 0:
                    M[i][j], M[i + 1][j] = M[i + 1][j], M[i][j]


def game(arr, M):
    kill = 0
    while True:
        if isNoEnemy(M):
            break
        kill_idx = set()
        for i in range(3):
            q = deque()
            y, x = R, arr[i]
            visited = [[False for _ in range(C)] for _ in range(R + 1)]
            q.append([y, x, 0])
            visited[y][x] = True

            while q:
                y, x, d = q.popleft()
                if d > D:
                    continue
                if M[y][x] == 1:
                    kill_idx.add(y * C + x)
                    break
                for dir in range(3):
                    ty, tx = y + dy[dir], x + dx[dir]
                    if ty < 0 or tx < 0 or tx >= C: continue
                    if not visited[ty][tx]:
                        if M[ty][tx] != 2:
                            q.append([ty, tx, d + 1])

        kill += len(kill_idx)
        kill_idx = list(kill_idx)
        for i in range(len(kill_idx)):
            y, x = kill_idx[i] // C, kill_idx[i] % C
            M[y][x] = 0
        move(M)

    return kill



R, C, D = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)] + [[2] * C]
check = [False for _ in range(R * C)]
dy = [0, -1, 0]; dx = [-1, 0, 1]  # 왼 -> 위 -> 오
arr = []
max_kill = -1
combi(0, 0)
print(max_kill)
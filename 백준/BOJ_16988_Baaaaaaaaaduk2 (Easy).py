from itertools import combinations


def make_new(a, b):
    for i in range(R):
        for j in range(C):
            if [i, j] == a or [i, j] == b:
                new_MAP[i][j] = 1
            else:
                new_MAP[i][j] = MAP[i][j]


def dfs(y, x):
    global flag, cnt
    visited[y][x] = True
    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= R or tx < 0 or tx >= C: continue
        if not visited[ty][tx]:
            if new_MAP[ty][tx] == 2:
                visited[ty][tx] = True
                cnt += 1
                dfs(ty, tx)
            elif new_MAP[ty][tx] == 0:
                flag = False


R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
result = -1
empty = []
for i in range(R):
    for j in range(C):
        if MAP[i][j] == 0:
            empty.append(i * C + j)

for comb in combinations(empty, 2):
    a, b = [comb[0] // C, comb[0] % C], [comb[1] // C, comb[1] % C]
    new_MAP = [[0 for _ in range(C)] for _ in range(R)]
    make_new(a, b)
    visited = [[False for _ in range(C)] for _ in range(R)]
    sub_result = 0
    for i in range(R):
        for j in range(C):
            if new_MAP[i][j] == 2 and not visited[i][j]:
                flag, cnt = True, 1
                dfs(i, j)
                if flag: sub_result += cnt
    if sub_result > result:
        result = sub_result

print(result)

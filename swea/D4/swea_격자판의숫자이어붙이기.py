import sys
sys.setrecursionlimit(1000000)

def dfs(y, x, path):
    if len(path) == 7:
        S.add(''.join(map(str, path)))
        return

    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= 4 or tx < 0 or tx >= 4: continue
        path.append(MAP[ty][tx])
        dfs(ty, tx, path)
        path.pop()


TC = int(input())
for tc in range(TC):
    MAP = [list(map(int, input().split())) for _ in range(4)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]

    S = set()
    for i in range(4):
        for j in range(4):
            dfs(i, j, [])
    print(len(S))
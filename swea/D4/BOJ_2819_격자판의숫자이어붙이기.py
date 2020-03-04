def dfs(y, x, index, s):
    global count
    if index == 7:
        result.add(s)
        return

    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= 4 or tx < 0 or tx >= 4: continue
        dfs(ty, tx, index + 1, s + MAP[ty][tx])


TC = int(input())
for tc in range(TC):
    MAP = [list(map(str, input().split())) for _ in range(4)]
    check = [[False for _ in range(10)] for _ in range(7)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    result = set()
    for r in range(4):
        for c in range(4):
            s = MAP[r][c]
            count = 0
            dfs(r, c, 1, s)

    print('#{} {}'.format(tc + 1, len(result)))

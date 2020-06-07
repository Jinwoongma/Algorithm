def dfs(y, x, index):
    if index == 6:
        temp = ''.join(map(str, arr))
        if len(result) == 0:
            result.append(temp)
            return
        else:
            if temp not in result:
                result.append(temp)
                return
            else: return

    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 0 or ty >= 5 or tx < 0 or tx >= 5: continue
        arr.append(MAP[y][x])
        dfs(ty, tx, index + 1)
        arr.pop()

MAP = [list(map(int, input().split())) for _ in range(5)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]

result = []
for i in range(5):
    for j in range(5):
        arr = []
        dfs(i, j, 0)

print(len(result))
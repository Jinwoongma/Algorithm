def dfs(index):
    global result
    print(result)

    if index == r * c:
        return
    y = index // c - 1
    x = index % c - 1

    if not visited[y][x]:
        x_diff = c - x - 1
        y_diff = r - y - 1

        for i in range(x_diff + 1):
            temp = ''
            ty, tx= y, x
            count = 0
            for j in range(i):
                ty += dy[1]
                tx += dx[1]
                if not visited[ty][tx]:
                    temp += MAP[ty][tx]
                    visited[ty][tx] = True
                    count += 1
                if len(temp) != 0:
                    result += int(temp)
                dfs(index + 1)
                for k in range(count):
                    visited[ty][tx] = False
                    ty -= dy[1]
                    tx -= dx[1]
                if len(temp) != 0:
                    result -= int(temp)


        for i in range(y_diff + 1):
            temp = ''
            ty, tx = y, x
            count = 0
            for j in range(i):
                ty += dy[0]
                tx += dx[0]
                if not visited[ty][tx]:
                    temp += MAP[ty][tx]
                    visited[ty][tx] = True
                    count += 1
                if len(temp) != 0:
                    result += int(temp)

                dfs(index + 1)

                for k in range(count):
                    visited[ty][tx] = False
                    ty -= dy[0]
                    tx -= dx[0]
                if len(temp) != 0:
                    result -= int(temp)

    else:
        dfs(index + 1)


r, c = map(int, input().split())
MAP = [list(map(str, input().strip())) for _ in range(r)]
visited = [[False for _ in range(c)] for _ in range(r)]
dy = [1, 0]; dx = [0, 1]
ind_MAP = []
for i in range(r):
    ind_MAP += MAP[i]
print(ind_MAP)

result = 0
dfs(0)
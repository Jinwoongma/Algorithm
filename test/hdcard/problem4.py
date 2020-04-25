dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
MAP = [[0 for _ in range(7)] for _ in range(7)]
path = []


def dfs(y, x, visited, ref):
    global path
    visited[y][x] = True
    for dir in range(4):
        ty, tx = y + dy[dir], x + dx[dir]
        if ty < 1 or ty >= 7 or tx < 1 or tx >= 7: continue
        if MAP[ty][tx] == ref and not visited[ty][tx]:
            path.append([ty, tx])
            dfs(ty, tx, visited, ref)


def update():
    for x in range(6, 0, -1):
        S = []
        for y in range(6, 0, -1):
            if MAP[y][x] != 0:
                S.append(MAP[y][x])
                MAP[y][x] = 0
        y = 6
        while S:
            temp = S.pop()
            MAP[y][x] = temp
            y -= 1


def solution(macaron):
    global path
    answer = []
    for x, color in macaron:
        for i in range(1, 7):
            if MAP[i][x] != 0:
                MAP[i - 1][x] = color
                y = i - 1
                break
        else:
            MAP[6][x] = color
            y = 6

        visited = [[False for _ in range(7)] for _ in range(7)]
        path = [[y, x]]
        dfs(y, x, visited, color)
        if len(path) >= 3:
            for y, x in path:
                MAP[y][x] = 0
            update()
            while True:
                visited = [[False for _ in range(7)] for _ in range(7)]
                flag = False
                for i in range(1, 7):
                    for j in range(1, 7):
                        if not visited[i][j] and MAP[i][j] != 0:
                            path = [[i, j]]
                            dfs(i, j, visited, MAP[i][j])
                            if len(path) >= 3:
                                flag = True
                                for y, x in path:
                                    MAP[y][x] = 0
                            update()
                if not flag: break
        print(y, x)
        for i in range(1, 7):
            print(MAP[i])
        print()

    for i in range(1, 7):
        answer.append(''.join(map(str, MAP[i][1:7])))
    return answer


a = [[1,1],[1,2],[1,4],[2,1],[2,2],[2,3],[3,4],[3,1],[3,2],[3,3],[3,4],[4,4],[4,3],[5,4],[6,1]]
print(solution(a))
from _collections import deque

dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
MAP = [[0 for _ in range(7)] for _ in range(7)]
path = []

def bfs(y, x, visited, ref):
    global path
    Q = deque()
    Q.append([y, x])
    visited[y][x] = True
    while Q:
        y, x = Q.popleft()
        for dir in range(4):
            ty, tx = y + dy[dir], x + dx[dir]
            if ty < 1 or ty >= 7 or tx < 1 or tx >= 7: continue
            if MAP[ty][tx] == ref and not visited[ty][tx]:
                visited[ty][tx] = True
                path += [[ty, tx]]
                Q.append([ty, tx])


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
        print(x, color)
        for i in range(1, 7):
            if MAP[i][x] != 0:
                MAP[i - 1][x] = color
                break
        else:
            MAP[6][x] = color

        while True:
            visited = [[False for _ in range(7)] for _ in range(7)]
            del_path = []
            for i in range(1, 7):
                for j in range(1, 7):
                    if MAP[i][j] != 0 and not visited[i][j]:
                        path = [[i, j]]
                        bfs(i, j, visited, MAP[i][j])
                        print(path)
                        if len(path) >= 3:
                            del_path += path

            if len(del_path) == 0:
                break

            for i in range(len(del_path)):
                MAP[del_path[i][0]][del_path[i][1]] = 0
            update()

        for i in range(1, 7):
            print(MAP[i][1:])
        print()

    for i in range(1, 7):
        answer.append(''.join(map(str, MAP[i][1:7])))
    return answer


a = [[1,1],[1,2],[1,4],[2,1],[2,2],[2,3],[3,4],[3,1],[3,2],[3,3],[3,4],[4,4],[4,3],[5,4],[6,1]]
print(solution(a))
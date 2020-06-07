def combi(index, start):
    global min_result
    if index == r:
        result = 0
        for i in range(len(house)):
            distance = []
            for j in range(len(open)):
                distance.append((abs(open[j][0] - house[i][0]) + abs(open[j][1] - house[i][1])))
            result += min(distance)
        min_result = min(result, min_result)
        return

    for i in range(start, L):
        open.append(chicken[i])
        combi(index + 1, i + 1)
        open.pop()


N, M = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dy = [1, -1, 0, 0]; dx = [0, 0, -1, 1]
chicken, house = [], []
result = 0
min_result = 0xffffffff
for i in range(N):
    for j in range(N):
        if MAP[i][j] == 2: chicken.append([i, j])
        elif MAP[i][j] == 1: house.append([i, j])

L = len(chicken)
for i in range(1, M + 1):
    open = []
    r = i
    result = 0
    combi(0, 0)

print(min_result)

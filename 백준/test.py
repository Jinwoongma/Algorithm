dx = [0, 1, 1, 1, 0, -1, -1, -1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]


def passed():
    deadtree = []
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if trees[i][j]:
                trees[i][j].sort()
                for t in range(len(trees[i][j])):
                    if land[i][j] >= trees[i][j][t]:
                        land[i][j] -= trees[i][j][t]
                        trees[i][j][t] += 1
                    else:
                        deadtree.append((i, j, trees[i][j][t]))

    for r, c, dt in deadtree:
        land[r][c] += dt // 2

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            cnt = 0
            if trees[i][j]:
                for t in range(len(trees[i][j])):
                    if not trees[i][j][t]:
                        cnt += 1
                        continue
                    if not trees[i][j][t] % 5:
                        for d in range(8):
                            tx, ty = i + dx[d], j + dy[d]
                            if 0 < tx < N + 1 and 0 < ty < N + 1:
                                trees[tx][ty].append(1)
            trees[i][j].sort()
            for d in range(cnt):
                trees[i][j].pop(0)

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if nutrients[i][j]:
                land[i][j] += nutrients[i][j]


N, M, K = map(int, input().split())
land = [[0] * (N+1)] + [[0] + [5] * N for _ in range(N)]
nutrients = [[0] * (N+1)] + [[0]+[*map(int, input().split())]
                             for _ in range(N)]
trees = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
result = 0
for m in range(M):
    x, y, z = map(int, input().split())
    trees[x][y].append(z)

for k in range(K):
    passed()

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if sum(trees[i][j]) > 0:
            result += len(trees[i][j])
print(result)
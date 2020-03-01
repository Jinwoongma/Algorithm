N, M, k = map(int, input().split())  # N: 면적, M: 나무의 개수, K: 년수
A = [list(map(int, input().split())) for _ in range(N)]  # 매년 추가되는  양분
food = [[5 for _ in range(N + 1)] for _ in range(N + 1)]
trees = [[[] for _ in range(N + 1)] for _ in range(N + 1)]
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]

for i in range(M):
    y, x, z = map(int, input().split())
    trees[y][x].append(z)

for i in range(k):  # k년 동안 반복
    # 봄
    death = []
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if len(trees[r][c]) != 0:
                trees[r][c].sort()
                temp = []
                for k in range(len(trees[r][c])):
                    if food[r][c] >= trees[r][c][k]:
                        food[r][c] -= trees[r][c][k]
                        temp.append(trees[r][c][k] + 1)
                    else:
                        death.append([r, c, trees[r][c][k]])
                trees[r][c] = temp[:]

    # 여름
    for y, x, age in death:
        food[y][x] += (age // 2)

    # 가을
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if len(trees[r][c]) != 0:
                for k in range(len(trees[r][c])):
                    if trees[r][c][k] % 5 == 0:
                        for dir in range(8):
                            ty, tx = r + dy[dir], c + dx[dir]
                            if ty < 1 or ty > N or tx < 1 or tx > N: continue
                            trees[ty][tx].append(1)

    # 겨울
    count = 0
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            food[r][c] += A[r - 1][c - 1]
            if len(trees[r][c]) != 0:
                count += len(trees[r][c])

print(count)

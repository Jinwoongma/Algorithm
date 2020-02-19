def dfs(cctv, index):
    if index == len(cctv):
        pass

    if cctv[index][2] == 1:


r, c = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(r)]
cctv = []
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

for i in range(r):
    for j in range(c):
        if 1 <= MAP[i][j] <= 5:
            cctv.append([i, j, MAP[i][j]])

print(cctv)

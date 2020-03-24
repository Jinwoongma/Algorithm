from itertools import combinations

N, M, G, R = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
possible = []
result = -1

for i in range(N):
    for j in range(M):
        if MAP[i][j] == 2:
            possible.append(i * M + j)

for G_loc in combinations(possible, G):
    new_posible = [i for i in possible if i not in G_loc]
    for R_loc in combinations(new_posible, R):
        sub_result = 0
        flower = []

        # Q에서 1이면 초록색, 2이면 빨강색
        visited = [[False for _ in range(M)] for _ in range(N)]
        Q = []
        for i in G_loc:
            Q.append([i, 1])
            visited[i // M][i % M] = True
        for i in R_loc:
            Q.append([i, 2])
            visited[i // M][i % M] = True

        while True:
            new_G, new_R = set(), set()
            for i in range(len(Q)):
                idx, color = Q[i]
                y, x = idx // M, idx % M
                for dir in range(4):
                    ty, tx = y + dy[dir], x + dx[dir]
                    if ty < 0 or ty >= N or tx < 0 or tx >= M: continue
                    if not visited[ty][tx] and MAP[ty][tx] != 0:
                        if color == 1:
                            new_G.add(ty * M + tx)
                        else:
                            new_R.add(ty * M + tx)

            if len(new_R) == 0 and len(new_R) == 0:
                break

            for i in new_G:
                visited[i // M][i % M] = True
            for i in new_R:
                visited[i // M][i % M] = True

            for i in new_G:
                for j in new_R:
                    if i == j and i not in flower:
                        flower.append(i)
                        sub_result += 1

            P = []
            for i in new_G:
                if i not in flower:
                    P.append([i, 1])
            for i in new_R:
                if i not in flower:
                    P.append([i, 2])

            Q = P

        result = max(result, sub_result)
print(result)

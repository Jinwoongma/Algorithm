from itertools import permutations
from copy import deepcopy


def turn(r, c, s):
    for i in range(s, 0, -1):
        y, x = r - i, c - i
        ty, tx, d = y, x, 3
        temp = newMAP[ty][tx]
        while True:
            ty = y + dy[d]
            tx = x + dx[d]
            if tx > c + i:
                tx -= dx[d]
                d = 1
                ty += dy[d]
                tx += dx[d]

            elif ty > r + i:
                ty -= dy[d]
                d = 2
                ty += dy[d]
                tx += dx[d]

            elif tx < c - i:
                tx -= dx[d]
                d = 0
                ty += dy[d]
                tx += dx[d]

            elif ty < r - i:
                break

            newMAP[ty][tx], temp = temp, newMAP[ty][tx]
            y, x = ty, tx


R, C, K = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
dy = [-1, 1, 0 , 0]; dx = [0, 0, -1, 1]
data = []
result = 0xfffff
for i in range(K):
    r, c, s = map(int, input().split())
    data.append([r - 1, c - 1, s])

for perm in permutations(data, K):
    newMAP = deepcopy(MAP)
    for i in range(len(perm)):
        r, c, s = perm[i]
        turn(r, c, s)

    sub_result = 0xfffff
    for j in range(R):
        sub_result = min(sub_result, sum(newMAP[j]))

    result = min(result, sub_result)


print(result)

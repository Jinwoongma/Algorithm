from _collections import deque


def isAllClear():
    for i in range(N):
        for j in range(M):
            if pan[i][j] > 0:
                return False
    return True


N, M, T = map(int, input().split())
pan = [deque(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
while T > 0:
    x, d, k = map(int, input().split())
    for i in range(1, N + 1):
        if i % x == 0:
            if d == 0:
                pan[i - 1].rotate(k % M)
            else:
                pan[i - 1].rotate(-1 * (k % M))

    if isAllClear():
        break
    else:
        DEL = set()
        for i in range(N):
            for j in range(M):
                if pan[i][j] == -1: continue
                for dir in range(4):
                    ty, tx = i + dy[dir], j + dx[dir]
                    if ty < 0 or ty >= N: continue
                    if tx < 0: tx = M - 1
                    elif tx >= M: tx = 0

                    if pan[i][j] == pan[ty][tx]:
                        DEL.add(i * M + j)
                        DEL.add(ty * M + tx)
        if len(DEL) == 0:
            SUM, cnt = 0, 0
            for i in range(N):
                for j in range(M):
                    if pan[i][j] != -1:
                        cnt += 1
                        SUM += pan[i][j]
            avg = SUM / cnt
            for i in range(N):
                for j in range(M):
                    if pan[i][j] != -1:
                        if pan[i][j] > avg:
                            pan[i][j] -= 1
                        elif pan[i][j] < avg:
                            pan[i][j] += 1
        else:
            for idx in DEL:
                pan[idx // M][idx % M] = -1
    T -= 1

answer = 0
for i in range(N):
    for j in range(M):
        if pan[i][j] != -1:
            answer += pan[i][j]
print(answer)
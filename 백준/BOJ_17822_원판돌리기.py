def turn(index, d, k):
    k = k % M
    if d == 0:
        pan[index][:k], pan[index][k:] = pan[index][M - k:M], pan[index][:M - k]
    elif d == 1:
        pan[index][:M - k], pan[index][M - k:M] = pan[index][k:], pan[index][:k]


N, M, T = map(int, input().split())  # N:원판개수, M: 원판에 적힌 수, T: 회전 수
pan = [[0] * N] + [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
for i in range(T):
    x, d, k = map(int, input().split())  #: x의 배수인 원판을 d 방향으로 k 칸 회전
    for j in range(1, N + 1):
        if j % x == 0:
            turn(j, d, k)

    # 인접한 수 찾기
    flag = False
    D = []
    for r in range(1, N + 1):
        for c in range(M):
            if pan[r][c] == 0: continue
            for dir in range(4):
                ty, tx = r + dy[dir], c + dx[dir]
                if ty < 1 or ty > N : continue
                if tx < 0: tx = M - 1
                if tx >= M: tx = 0
                if pan[r][c] == pan[ty][tx]:
                    D.append([r, c])
                    D.append([ty, tx])
                    flag = True
    for m in range(len(D)):
        pan[D[m][0]][D[m][1]] = 0

    # 인접한 수가 없다면면
    if not flag:
        SUM, num = 0, 0
        for r in range(1, N + 1):
            for c in range(M):
                if pan[r][c] != 0:
                    SUM += pan[r][c]
                    num += 1
        if num != 0:
            avg = SUM / (num)  # 나눗셈 할떄 항상 조심!! (0으로 나눌 경우)

        for r in range(1, N + 1):
            for c in range(M):
                if pan[r][c] == 0: continue
                if pan[r][c] > avg: pan[r][c] -= 1
                elif pan[r][c] < avg: pan[r][c] += 1
SUM = 0
for r in range(1, N + 1):
    for c in range(M):
       SUM += pan[r][c]
print(SUM)

import sys
sys.stdin = open('input.txt', 'r')

def calc(index, start):
    global min_diff
    if index == N // 2:
        A, B = [], []
        for j in range(N):
            if visited[j]:
                A.append(j)
            else:
                B.append(j)
        # print(A, B)
        A_score, B_score, diff = 0, 0, 0
        for i in range(N // 2 - 1):
            for j in range(i, N // 2):
                A_score += (MAP[A[i]][A[j]] + MAP[A[j]][A[i]])
                B_score += (MAP[B[i]][B[j]] + MAP[B[j]][B[i]])
        diff = abs(A_score - B_score)
        min_diff = min(diff, min_diff)
        return
    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            calc(index + 1, i)
            visited[i] = False

TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    min_diff = 0xffffffff
    calc(0, 0)
    print('#{} {}'.format(tc + 1, min_diff))
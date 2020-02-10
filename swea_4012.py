import sys
sys.stdin = open("input_4012.txt", "r")

def combination(index, cnt):
    if cnt == N // 2:
        for i in range(N):
            if select[i]:
                A.append(arr[i])
            else:
                B.append(arr[i])

    for i in range(index, N):
        if select[i]:
            continue
        select[i] = True
        combination(i, cnt+1)
        select[i] = False


TC = int(input())
for tc in range(TC):
    N = int(input())
    min_diff = 400000
    S = []
    for i in range(N):
        line = list(map(int, input().split()))
        S.append(line)

    arr = list(range(1, N+1))
    select = [False for i in range(N)]
    A, B = [], []
    combination(0, 0)

    for i in range(int(len(A)/(N//2))):
        temp_A = A[i * (N // 2) : i * (N // 2) + (N // 2)]
        temp_B = B[i * (N // 2) : i * (N // 2) + (N // 2)]
        A_sum, B_sum = 0, 0
        for j in range(len(temp_A)):
            for k in range(j+1, len(temp_A)):
                A_sum += S[temp_A[j] - 1][temp_A[k] - 1] + S[temp_A[k] - 1][temp_A[j] - 1]
                B_sum += S[temp_B[j] - 1][temp_B[k] - 1] + S[temp_B[k] - 1][temp_B[j] - 1]
            diff = abs(A_sum - B_sum)
        if diff <= min_diff:
            min_diff = diff

    print('#{} {}'.format(tc+1, min_diff))

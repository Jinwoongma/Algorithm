TC = int(input())
for tc in range(TC):
    N, K = map(int, input().split())
    check = [False] * N
    submission = list(map(int, input().split()))
    for i in range(K):
        check[submission[i]-1] = True
    result = [i + 1 for i in range(N) if not check[i]]
    print('#{} {}'.format(tc + 1, ' '.join(map(str, result))))

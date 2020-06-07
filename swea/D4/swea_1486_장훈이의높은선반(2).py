

TC = int(input())
for tc in range(TC):
    N, B = map(int, input().split())
    h = list(map(int, input().split()))
    visited = [False for _ in range(N)]
    min_diff = 0xffffffff

    for i in range(1 << N):
        SUM = 0
        for j in range(N):
            if i & (1 << j):
                SUM += h[j]
            if SUM >= B:
                min_diff = min(min_diff, SUM - B)
                break
    print('#{} {}'.format(tc + 1, min_diff))
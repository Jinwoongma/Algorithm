TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    box = list(map(int, input().split()))
    bus = list(map(int, input().split()))
    check = [False for _ in range(N)]

    ans = 0
    for i in range(M):
        sub_result = 0
        index = 0
        for j in range(N):
            if bus[i] >= box[j] and box[j] >= sub_result and not check[j]:
                sub_result = box[j]
                index = j
        if sub_result != 0:
            check[index] = True
        ans += sub_result

    print('#{} {}'.format(tc + 1, ans))
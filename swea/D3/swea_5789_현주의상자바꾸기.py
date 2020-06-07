TC = int(input())
for tc in range(TC):
    N, Q = map(int, input().split())
    box = [0] * (N + 1)

    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            box[j] = i

    print('#{} {}'.format(tc + 1, ' '.join(map(str, box))))



TC = int(input())
for tc in range(TC):
    N = int(input())
    cards = list(map(str, input().split()))
    shuffle = []
    if N % 2:
        A, B = cards[:N // 2 + 1], cards[N // 2 + 1:]
        shuffle.append(A[0])
        for i in range(len(B)):
            shuffle.append(B[i])
            shuffle.append(A[i + 1])
    else:
        A, B = cards[:N // 2], cards[N // 2:]
        for i in range(len(A)):
            shuffle.append(A[i])
            shuffle.append(B[i])
    print('#{} {}'.format(tc + 1, ' '.join(shuffle)))

TC = int(input())
for tc in range(TC):
    N = int(input())

    line = []
    for i in range(N):
        line.append(list(map(int, input().split())))
    P = int(input())

    stop = []
    for i in range(P):
        stop.append(int(input()))

    check = [0] * P
    for i in range(N):
        for j in range(P):
            if line[i][0] <= stop[j] <= line[i][1]:
                check[j] += 1

    print('#{} {}'.format(tc + 1, ' '.join(map(str, check))))

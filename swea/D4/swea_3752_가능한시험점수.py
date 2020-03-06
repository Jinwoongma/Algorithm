TC = int(input())
for tc in range(TC):
    N = int(input())
    num = list(map(int, input().split()))
    check = [0] * 10001
    SUM = sum(num)

    check[0] = 1
    for i in range(N):
        for j in range(SUM, -1, -1):
            if check[j]:
                check[j + num[i]] = 1

    print('#{} {}'.format(tc + 1, sum(check)))
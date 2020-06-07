for tc in range(1, 11):
    N = int(input())
    data = [str(input()) for _ in range(8)]
    count = 0

    # 가로 탐색
    for i in range(8):
        for j in range(8 - N + 1):
            temp = data[i][j:j + N]
            if temp == ''.join(reversed(temp)):
                count += 1

    # 세로 탐색
    for i in range(8):
        for j in range(8 - N + 1):
            temp = ''
            for k in range(N):
                temp += data[j + k][i]
            if temp == ''.join(reversed(temp)):
                count += 1

    print('#{} {}'.format(tc, count))

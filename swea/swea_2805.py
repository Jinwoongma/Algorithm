TC = int(input())
for tc in range(TC):
    N = int(input())
    count_sum = 0
    data = [str(input()) for _ in range(N)]

    # 중간 이전 계산
    for i in range(N):
        temp = data[i]
        if i <= int(N / 2):
            start = (int(N / 2)) - i
            end = (int(N / 2)) + i + 1
            for j in range(start, end):
                count_sum += int(temp[j])

        # 중간부 계산
        elif i == int(N / 2):
            for j in range(N):
                count_sum += int(temp[j])

        # 중간 이후 계산
        else:
            start = int(N / 2) - (N - 1 - i)
            end = (int(N / 2)) + (N - i)
            for j in range(start, end):
                count_sum += int(temp[j])

    print('#{} {}'.format(tc + 1, count_sum))
def check(arr):
    N = len(arr)
    count = 0
    for i in range(N):
        if sum(arr[i]) == 0:
            count += 1

    for i in range(N):
        sum_ = 0
        for j in range(N):
            sum_ += arr[j][i]
        if sum_ == 0:
            count += 1

    sum_ = 0
    for i in range(N):
        sum_ += arr[i][i]
    if sum_ == 0:
        count += 1

    sum_ = 0
    for i in range(N):
        sum_ += arr[i][4-i]
    if sum_ == 0:
        count += 1

    return count


bingo = [list(map(int, input().split())) for _ in range(5)]
calls = []
for i in range(5):
    calls += list(map(int, input().split()))
# print(calls)
for i in range(1, 26):
    number = calls[i-1]
    for j in range(5):
        for k in range(5):
            if bingo[j][k] == number:
                bingo[j][k] = 0

    # for j in range(5):
    #     print(bingo[j])
    # print()

    if check(bingo) >= 3:
        print(i)
        break


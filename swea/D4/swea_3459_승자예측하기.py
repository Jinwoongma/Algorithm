TC = int(input())
for tc in range(TC):
    N = int(input())
    check = 0
    turn, mul = 1, 1

    while turn < N:
        if not check:
            mul *= 4
        turn += mul
        check = not check

    if check:
        print('#{} Alice'.format(tc + 1))
    else:
        print('#{} Bob'.format(tc + 1))

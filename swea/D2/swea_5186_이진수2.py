TC = int(input())
for tc in range(TC):
    N = float(input())
    m = 1
    result = ''
    while m < 14:
        mok = N // (2 ** (-m))
        N = N - mok * (2 ** (-m))
        result += str(int(mok))
        if N == 0: break
        m += 1

    if m >= 13:
        answer = 'overflow'
    else:
        answer = result
    print('#{} {}'.format(tc + 1, answer))
import sys
sys.stdin = open('input_1860.txt', 'r')

TC = int(input())
for tc in range(TC):
    N, M, K = map(int, input().split())
    comes = list(map(int, input().split()))
    comes.sort()

    last_come = comes[-1]
    remain = [0] * last_come
    baseline = 0
    for i in range(len(remain)):
        if i % M == 0 and i != 0:
            baseline += K
        remain[i] += baseline
    # print(remain)

    flag = True
    for come in comes:
        if flag == True:
            for i in range(come, len(remain)):
                remain[i] -= 1
                if remain[i] < 0:
                    flag = False
                    break
            if come < M:
                flag = False
        else:
            break

    if flag == True:
        print('#{} Possible'.format(tc+1))
    else:
        print('#{} Impossible'.format(tc + 1))

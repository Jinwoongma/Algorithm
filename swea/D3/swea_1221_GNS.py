import sys
sys.stdin = open('input_1221.txt', 'r')

TC = int(input())
code = [('ZRO', 0), ('ONE', 1), ('TWO', 2), ('THR', 3), ('FOR', 4)
        , ('FIV', 5), ('SIX', 6), ('SVN', 7), ('EGT', 8), ('NIN', 9)]

for tc in range(TC):
    t, N = map(str, input().split())
    N = int(N)
    data = list(map(str, input().split()))

    for num in code:
        for i in range(len(data)):
            if data[i] == num[0]:
                data[i] = num[1]
    data.sort()
    for num in code:
        for i in range(len(data)):
            if data[i] == num[1]:
                data[i] = num[0]
    print('#{}'.format(tc + 1))
    print(' '.join(data))
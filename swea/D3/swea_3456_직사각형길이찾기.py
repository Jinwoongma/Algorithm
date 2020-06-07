import sys
sys.stdin = open('input_3456.txt', 'r')

TC = int(input())
for tc in range(TC):
    data = list(map(int, input().split()))
    data.sort()
    S = []
    for i in range(len(data)):
        if len(S) == 0:
            S.append(data[i])
        else:
            if data[i] == S[-1]:
                S.pop()
            else:
                S.append(data[i])
    print('#{} {}'.format(tc + 1, S[0]))



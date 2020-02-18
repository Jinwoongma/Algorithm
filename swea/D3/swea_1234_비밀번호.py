import sys
sys.stdin = open('input_1234.txt', 'r')

for tc in range(10):
    L, code = map(str, input().split())
    L = int(L)
    S = []
    for i in range(L):
        if len(S) == 0: S.append(code[i])
        else:
            if code[i] != S[-1]:
                S.append(code[i])
            else:
                S.pop()
    print('#{} {}'.format(tc + 1, ''.join(S)))
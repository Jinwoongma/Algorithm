import sys
sys.stdin = open('input_4873.txt', 'r')
TC = int(input())
for tc in range(TC):
    data = str(input())
    S = []
    for char in data:
        if len(S) == 0:
            S.append(char)
        else:
            if char == S[-1]:
                S.pop()
            else:
                S.append(char)

    print('#{} {}'.format(tc + 1, len(S)))
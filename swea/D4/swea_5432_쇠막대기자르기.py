import sys
sys.stdin = open('input_5432.txt', 'r')
TC = int(input())
for tc in range(TC):
    data = input()
    S = []
    data = data.replace('()', '.')
    result = 0

    for i in range(len(data)):
        if data[i] == '(':
            S.append([data[i], i])
        if len(S) != 0:
            if data[i] == ')':
                start = S.pop()
                count = 0
                for j in range(start[1], i):
                    if data[j] == '.':
                        count += 1
                result += (count + 1)

    print('#{} {}'.format(tc + 1, result))

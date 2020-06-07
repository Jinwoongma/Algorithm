import sys
sys.stdin = open('input_5948.txt', 'r')

TC = int(input())
for tc in range(TC):
    data = list(map(int, input().split()))
    result = []
    for i in range(7):
        for j in range(i + 1, 7):
            for k in range(j + 1, 7):
                result.append(data[i] + data[j] + data[k])
    result = list(set(result))
    result.sort(reverse=True)
    if len(result) >= 5:
        print('#{} {}'.format(tc + 1, result[4]))
    else:
        print('#{} {}'.format(tc + 1, result[-1]))
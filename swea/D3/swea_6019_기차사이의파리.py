TC = int(input())
for tc in range(TC):
    D, A, B, F = map(int, input().split())
    result = (D / (A + B)) * F
    print('#{} {}'.format(tc + 1, result))
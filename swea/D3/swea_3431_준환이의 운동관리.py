TC = int(input())
for tc in range(TC):
    L, U, X = map(int, input().split())
    if L > X:
        print('#{} {}'.format(tc + 1, L-X))
    elif L <= X <= U:
        print('#{} {}'.format(tc + 1, 0))
    elif X > U:
        print('#{} {}'.format(tc + 1, -1))
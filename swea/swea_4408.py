import sys
sys.stdin = open('input_4408.txt', 'r')

TC = int(input())
for tc in range(TC):
    N = int(input())
    data = [[0 for _ in range(201)] for _ in range(N)]
    count = [0 for _ in range(201)]

    for n in range(N):
        r1, r2 = map(int, input().split())
        if r1 > r2:
            r1, r2 = r2, r1
        if r1 % 2 == 1:
            r1 += 1
        if r2 % 2 == 1:
            r2 += 1
        r1 = r1 // 2
        r2 = r2 // 2

        for i in range(r1, r2 + 1):
            count[i] += 1

    print('#{} {}'.format(tc + 1, max(count)))
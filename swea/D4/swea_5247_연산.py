from _collections import deque

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    check = [False] * 1000050
    Q = deque()
    Q.append([N, 0])
    check[N] = True
    answer = 0
    while Q:
        n, t = Q.popleft()
        if n == M:
            answer = t
            break
        for i in [n + 1, n - 1, n * 2, n - 10]:
            if 0 <= i <= 1000010 and not check[i]:
                check[i] = True
                Q.append([i, t + 1])

    print('#{} {}'.format(tc + 1, answer))
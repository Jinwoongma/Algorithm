from collections import deque
TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))

    P = deque()  # 남은 피자
    for i in range(M):
        P.append((pizza[i], i + 1))
    Q = deque() # 화덕에 들어있는 피자
    for i in range(N):
        Q.append(P.popleft())

    while True:
        if len(P) == 0 and len(Q) == 1:
            print('#{} {}'.format(tc + 1, Q.popleft()[1]))
            break
        else:
            temp, idx = Q.popleft()
            temp = temp // 2
            if temp // 2 != 0:
                Q.append((temp, idx))
            else:
                if len(P) > 0:
                    Q.append(P.popleft())
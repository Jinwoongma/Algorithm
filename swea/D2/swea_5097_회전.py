from _collections import deque
TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    Q = deque()
    for i in range(N):
        Q.append(nums[i])

    Q.rotate(-1 * (M % N))

    print('#{} {}'.format(tc + 1, Q.popleft()))
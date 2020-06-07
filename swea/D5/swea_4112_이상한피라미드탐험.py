from _collections import deque

S, plus = [1], 1
while True:
    if S[-1] + plus > 10001:
        S.append(S[-1] + plus)
        plus += 1
        break
    else:
        S.append(S[-1] + plus)
        plus += 1


def find_row(num):
    for i in range(len(S) - 1):
        if S[i] <= num < S[i + 1]:
            l = S[i + 1] - S[i]
            if num == S[i]:
                next = [num + 1, num + l, num - l + 1, num + l + 1]
            elif num == S[i + 1] - 1:
                next = [num - 1, num - l, num + l, num + l + 1]
            else:
                next = [num - 1, num + 1, num - l, num + l, num - l + 1, num + l + 1]
            return next


def bfs(start, goal):
    global ans
    Q = deque()
    Q.append([start, 0])
    visited[start] = True
    while Q:
        cur, time = Q.popleft()
        if cur == goal:
            ans = time
            break
        next = find_row(cur)
        for n in next:
            if n <= 0 or n >= 10001: continue
            if not visited[n]:
                Q.append([n, time + 1])
                visited[n] = True
    return


TC = int(input())
for tc in range(TC):
    a, b = map(int, input().split())
    visited = [False] * 10001
    ans, flag = -1, False

    bfs(a, b)
    print('#{} {}'.format(tc + 1, ans))
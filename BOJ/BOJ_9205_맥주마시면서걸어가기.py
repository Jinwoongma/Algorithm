from _collections import deque
import math

TC = int(input())
for tc in range(TC):
    N = int(input())
    sy, sx = map(int, input().split())
    stop = [[sy, sx]]
    for i in range(N):
        stop.append(list(map(int, input().split())))
    ey, ex = map(int, input().split())
    stop.append([ey, ex])

    visited = [False for _ in range(N + 2)]
    G = [[] for _ in range(N + 2)]
    for i in range(N + 1):
        for j in range(i + 1, N + 2):
            if abs(stop[i][0] - stop[j][0]) + abs(stop[i][1] - stop[j][1]) <= 1000:
                G[i].append(j)
                G[j].append(i)

    Q = deque()
    Q.append(0)
    visited[0] = True
    flag = False
    while Q:
        stop_idx = Q.popleft()
        y, x = stop[stop_idx][0], stop[stop_idx][1]
        if y == ey and x == ex:
            print('happy')
            flag = True
            break

        for w in G[stop_idx]:
            if not visited[w]:
                visited[w] = True
                Q.append(w)

    if not flag:
        print('sad')
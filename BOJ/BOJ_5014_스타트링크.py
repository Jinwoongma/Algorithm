from _collections import deque

F, S, G, U, D = map(int, input().split())
visited = [0] * (F + 1)
Q = deque()
Q.append([S, 0])
visited[S] = True
flag = False
while Q:
    s, cnt = Q.popleft()
    if s == G:
        print(cnt)
        flag = True
        break
    else:
        if s + U <= F:
            if not visited[s + U]:
                visited[s + U] = 1
                Q.append([s + U, cnt + 1])
        if s - D >= 1:
            if not visited[s - D]:
                visited[s - D] = 1
                Q.append([s - D, cnt + 1])

if not flag:
    print('use the stairs')
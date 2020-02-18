from collections import deque

N, M = map(int, input().split())
visited = [False] * 300000
time = [0] * 300000
Q = deque()
Q.append(N)
visited[N] = True
# time[N] = 0

while Q:
    s = Q.popleft()
    if s == M:
        break

    if s - 1 >= 0 and not visited[s - 1]:
        Q.append(s - 1)
        visited[s - 1] = True
        time[s - 1] = time[s] + 1
    if s + 1 <= 100000 and not visited[s + 1]:
        Q.append(s + 1)
        visited[s + 1] = True
        time[s + 1] = time[s] + 1
    if s * 2 <= 100000 and not visited[s * 2]:
        Q.append(s * 2)
        visited[s * 2] = True
        time[s * 2] = time[s] + 1

print(time[M])
from _collections import deque

N, K = map(int, input().split())
data = [list(map(int, input().strip())) for _ in range(N)]
a, b = map(int, input().split())
G = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
flag = False

for i in range(N):
    for j in range(N):
        if i == j: continue
        count = 0
        for k in range(len(data[i])):
            if data[i][k] != data[j][k]: count += 1
        if count == 1:
            G[i + 1].append(j + 1)

Q = deque()
Q.append([a, [a]])
while Q:
    s, path = Q.popleft()
    visited[s] = True
    if s == b:
        print(' '.join(map(str, path)))
        flag = True
        break
    for w in G[s]:
        if not visited[w]:
            Q.append([w, path + [w]])

if not flag:
    print(-1)
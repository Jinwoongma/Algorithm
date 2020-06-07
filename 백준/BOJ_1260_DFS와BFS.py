from collections import deque

def dfs(v):
    visited[v] = True
    path.append(v)
    for w in G[v]:
        if not visited[w]:
            dfs(w)

def bfs(v):
    visited[v] = True
    Q = deque()
    Q.append(v)
    path.append(v)
    while Q:
        s = Q.popleft()
        for w in G[s]:
            if not visited[w]:
                Q.append(w)
                visited[w] = True
                path.append(w)

V, E, num = map(int, input().split())
G = [[] for _ in range(V + 1)]
for i in range(E):
    v, u = map(int, input().split())
    G[v].append(u)
    G[u].append(v)

for i in range(V):
    G[i].sort()

path = []
visited = [0 for _ in range(V + 1)]
dfs(num)
for i in range(len(path)):
    print(path[i], end=' ')
print()

path = []
visited = [0 for _ in range(V + 1)]
bfs(num)
for i in range(len(path)):
    print(path[i], end=' ')
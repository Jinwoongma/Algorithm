V = int(input())
E = int(input())

def dfs(v):
    visited[v] = True
    path.append(v)
    for w in G[v]:
        if not visited[w]:
            dfs(w)

G = [[] for _ in range(V + 1)]
visited = [False for _ in range(V+1)]
path = []

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

dfs(1)
print(len(path)-1)


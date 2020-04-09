# 21:36 ~ 21.51

def dfs(idx):
    global ans
    visited[idx] = True
    for w in G[idx]:
        if not visited[w]:
            ans += 1
            dfs(w)

N = int(input())
G = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
E = int(input())

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

ans = 0
dfs(1)
print(ans)
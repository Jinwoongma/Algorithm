def dfs(v, cnt):
    global ans
    if v == s2:
        ans = cnt
    visited[v] = True
    for w in G[v]:
        if not visited[w]:
            dfs(w, cnt + 1)

N = int(input())
s1, s2 = map(int, input().split())
E = int(input())
G = [[] for _ in range(N + 1)]
visited = [0 for _ in range(N + 1)]

for i in range(E):
    v, u = map(int, input().split())
    G[v].append(u)
    G[u].append(v)

ans = -1
dfs(s1, 0)
print(ans)
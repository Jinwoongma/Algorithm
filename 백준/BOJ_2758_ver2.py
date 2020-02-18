def bfs(v, count):
    if len(result) == r:
        print(result)
        return
    else:
        visited[v] = True
        result.append(v)
        for w in G[v]:
            if not visited[w]:
                bfs(w, count + 1)
                result.pop(-1)

TC = int(input())
for tc in range(TC):
    r, n = map(int, input().split())
    G = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    for i in range(n+1):
        for j in range(1, n+1):
            if j >= 2*i:
                G[i].append(j)

    result = []
    count = 0
    bfs(1, 0)
    print(result)
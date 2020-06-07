TC = int(input())

def dfs(x, l):
    check[x] = True
    result.append(l)
    for k in G[x]:
        if check[k] == False:
            dfs(k,l+1)
            check[k] = False

for tc in range(TC):
    V, E = map(int,input().split())
    G = [[] for _ in range(V + 1)]
    result = []
    for j in range(E):
        x, y = map(int, input().split())
        G[x].append(y)
        G[y].append(x)
    for p in range(V):
        check = [False] * (V + 1)
        dfs(p, 1)

    print('#{} {}'.format(tc + 1, max(result)))
import sys
sys.stdin = open('input_4871.txt', 'r')

def dfs(v):
    visited[v] = True
    # path.append(v)
    for w in G[v]:
        if not visited[w]:
            visited[w] = True
            dfs(w)

TC = int(input())
for tc in range(TC):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    visited = [0 for _ in range(V + 1)]

    for i in range(E):
        v, u = map(int, input().split())
        G[v].append(u)

    start, end = map(int, input().split())
    path = []
    dfs(start)
    if end in path:
        print('#{} {}'.format(tc + 1, 1))
    else:
        print('#{} {}'.format(tc + 1, 0))
import sys
sys.stdin = open("input_1219.txt", "r")
def dfs(v):
    visited[v] = True
    path.append(v)
    for w in G[v]:
        if not visited[w]:
            dfs(w)

for tc in range (10):
    path = []
    t, E = map(int, input().split())
    data = list(map(int, input().split()))
    G = [[] for _ in range(100)]
    visited = [False for _ in range(100)]

    u = [data[i] for i in range(len(data)) if i % 2 == 0]
    v = [data[i] for i in range(len(data)) if i % 2 == 1]

    for i in range(E):
        G[u[i]].append(v[i])

    dfs(0)
    # print(path)
    if 99 in path:
        print('#{} 1'.format(t))
    else:
        print('#{} 0'.format(t))
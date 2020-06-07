import heapq


def Dijkstra(G, start):
    D = [0xfffff] * (N + 1)
    h = []
    D[start] = 0
    heapq.heappush(h, (0, start))
    while h:
        d, cur_node = heapq.heappop(h)
        if d > D[cur_node]: continue
        for next_node, w in G[cur_node]:
            if D[next_node] > D[cur_node] + w:
                D[next_node] = D[cur_node] + w
                heapq.heappush(h, (D[next_node], next_node))
    return D


N, M, X = map(int, input().split())
go_G = [[] for _ in range(N + 1)]
back_G = [[] for _ in range(N + 1)]
result = -1
for i in range(M):
    u, v, w = map(int, input().split())
    go_G[u].append([v, w])
    back_G[v].append([u, w])

go_D = Dijkstra(go_G, X)
back_D = Dijkstra(back_G, X)
for i in range(1, N + 1):
    result = max(result,  go_D[i] + back_D[i])

print(result)
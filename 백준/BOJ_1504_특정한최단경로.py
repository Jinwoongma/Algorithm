import heapq

def Dijkstra(start):
    D = [MAX for _ in range(N + 1)]
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


N, E = map(int, input().split())
G = [[] for _ in range(N + 1)]
MAX = 0xffffff
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])
p1, p2 = map(int, input().split())

D1 = Dijkstra(1)
D2 = Dijkstra(p1)
D3 = Dijkstra(p2)
result1, result2 = MAX, MAX

if D1[p1] != MAX and D2[p2] != MAX and D3[N] != MAX:
    result1 = D1[p1] + D2[p2] + D3[N]
if D1[p2] != MAX and D3[p1] != MAX and D2[N] != MAX:
    result2 = D1[p2] + D3[p1] + D2[N]

if result1 >= MAX and result2 >= MAX:
    print(-1)
else:
    print(min(result1, result2))

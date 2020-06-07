import heapq

N = int(input())
M = int(input())
G = [[] for _ in range(N + 1)]
for i in range(M):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
s, e = map(int, input().split())

h = []
D = [10e10] * (N + 1)
heapq.heappush(h, (0, s))
D[s] = 0
while h:
    d, cur_node = heapq.heappop(h)
    if d > D[cur_node]: continue
    for next_node, w in G[cur_node]:
        if D[next_node] > D[cur_node] + w:
            D[next_node] = D[cur_node] + w
            heapq.heappush(h, (D[next_node], next_node))

print(D[e])
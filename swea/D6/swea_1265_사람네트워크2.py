import sys
sys.stdin = open('input.txt', 'r')
import heapq

def dijkstra(s):
    D = [0xfffff for _ in range(N + 1)]
    h = []
    D[s] = 0
    heapq.heappush(h, (0, s))
    while h:
        d, cur_node = heapq.heappop(h)
        if d > D[cur_node]: continue
        for w, next_node in G[cur_node]:
            if D[next_node] > D[cur_node] + w:
                D[next_node] = D[cur_node] + w
                heapq.heappush(h, (D[next_node], next_node))
    return sum(D[1:])


TC = int(input())
for tc in range(TC):
    data = list(map(int, sys.stdin.readline().split()))
    N = data[0]

    G = [[] for _ in range(N + 1)]
    for i in range(1, len(data)):
        if data[i] == 1:
            u, v = (i - 1) // N, (i - 1) % N
            G[u + 1].append([1, v + 1])
    result = 0xfffff
    for i in range(1, N + 1):
        result = min(result, dijkstra(i))

    print('#{} {}'.format(tc + 1, result))
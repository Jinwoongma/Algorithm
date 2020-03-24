# 1. 슈퍼컴퓨터를 시작점으로 다른 모든 node 까지의 최소 거리 D와 부모배열 P를 다익스트라로 구한다
# 1번 조건 의미 없음 -> 네트워크가 연결되려면 무조건 n-1개 간선필요하기 때문
# n-1개의 간선이 무엇인지 알기 위해서 P라는 부모 배열을 만들어서 그전에 연결된 점을 저장함
import heapq

def Dijkstra(start):
    D = [0xfffff for _ in range(N + 1)]
    P = [i for i in range(N + 1)]
    D[start] = 0
    h = []
    heapq.heappush(h, (0, start))
    while h:
        d, cur_node = heapq.heappop(h)
        if d > D[cur_node]: continue
        for next_node, w in G[cur_node]:
            if D[next_node] > D[cur_node] + w:
                D[next_node] = D[cur_node] + w
                P[next_node] = cur_node
                heapq.heappush(h, (D[next_node], next_node))
    return P

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for i in range(M):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

P = Dijkstra(1)
print(N - 1)
for i in range(2, N + 1):
    print('{} {}'.format(i, P[i]))
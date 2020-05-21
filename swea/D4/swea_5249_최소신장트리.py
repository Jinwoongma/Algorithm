import heapq

class DisjointSet:
    def __init__(self, n):
        self.data = [-1 for _ in range(n)]
        self.size = n

    def find(self, index):
        value = self.data[index]
        if value < 0:
            return index
        return self.find(value)

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.data[x] < self.data[y]:  # x가 더 큰 사이즈 -> x에 y를 더한다.
            self.data[x] += self.data[y]
            self.data[y] = x
        else:
            self.data[y] += self.data[x]
            self.data[x] = y
        self.size -= 1

# 1. Kruskal 알고리즘(disjoint-set 이용)
TC = int(input())
for tc in range(TC):
    V, E = map(int, input().split())
    result = 0
    G = []
    for i in range(E):
        u, v, w = map(int, input().split())
        G.append([u, v, w])
    G.sort(key=lambda weight: weight[2])
    disjoint = DisjointSet(V + 1)
    for data in G:
        u, v, w = data
        root1, root2 = disjoint.find(u), disjoint.find(v)
        if root1 != root2:
            disjoint.union(root1, root2)
            result += w

    print('#{} {}'.format(tc + 1, result))


# 2. heapq 를 이용한 prim 알고리즘
def mst_prim(G, r):
    h = []
    visited = [False] * (V + 1)
    D = [0xfffff] * (V + 1)
    D[r] = 0
    heapq.heappush(h, (0, r))
    while h:
        d, v = heapq.heappop(h)
        visited[v] = True
        for w, u in G[v]:
            if not visited[u] and w < D[u]:
                D[u] = w
                heapq.heappush(h, (w, u))
    return sum(D)


TC = int(input())
for tc in range(TC):
    V, E = map(int, input().split())
    G = [[] for _ in range(V + 1)]
    for i in range(E):
        u, v, w = map(int, input().split())
        G[u].append([w, v])
        G[v].append([w, u])

    result = mst_prim(G, 0)
    print('#{} {}'.format(tc + 1, result))
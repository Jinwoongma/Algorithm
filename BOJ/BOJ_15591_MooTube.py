from _collections import deque


def bfs(start, min):
    visited = [False for _ in range(N + 1)]
    Q = deque()
    Q.append(start)
    visited[start] = True
    ret = 0

    while Q:
        s = Q.popleft()
        ret += 1
        for w in G[s]:
            if not visited[w[0]] and w[1] >= min:
                visited[w[0]] = True
                Q.append(w[0])
    return ret - 1


N, Q = map(int, input().split())
G = [[] for _ in range(N + 1)]

for i in range(N - 1):
    p, q, r = map(int, input().split())
    G[p].append([q, r])
    G[q].append([p, r])

for i in range(Q):
    k, v = map(int, input().split())
    print(bfs(v, k))
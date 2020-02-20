# def dfs(v):
#     global count
#     visited[v] = True
#     for w in G[v]:
#         if not visited[w]:
#             count += 1
#             dfs(w)

from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    global count
    Q = deque()
    Q.append(v)
    visited[v] = True

    while Q:
        s = Q.popleft()
        for w in G[s]:
            if not visited[w]:
                count += 1
                Q.append(w)
                visited[w] = True

N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
arr = []
max_count = -1

for i in range(M):
    u, v = map(int, input().split())
    G[v].append(u)

for i in range(1, N + 1):
    visited = [0 for _ in range(N + 1)]
    count = 0
    bfs(i)
    if count > max_count:
        max_count = count
        arr.clear()
        arr.append(i)
    elif count == max_count:
        arr.append(i)
arr.sort()

print(' '.join(map(str, arr)))

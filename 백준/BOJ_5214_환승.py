from _collections import deque
import sys
input = sys.stdin.readline

N, K, M = map(int, input().split())
G = [[] for _ in range(N + M + 1)]
D = [0 for _ in range(N + M + 1)]
ans = False

for i in range(M):
    tube = list(map(int, input().split()))
    G[N + i + 1] = tube
    for j in range(K):
        G[tube[j]].append(N + i + 1)

Q = deque()
Q.append(1)
D[1] = 1
while Q:
    u = Q.popleft()
    if u == N:
        ans = D[u]
        break
    for w in G[u]:
        if not D[w]:
            if w > N:  # 하이퍼링크일때는 D 변화 없음
                D[w] = D[u]
                Q.append(w)
            else:
                D[w] = D[u] + 1
                Q.append(w)


if not ans:
    print(-1)
else:
    print(ans)
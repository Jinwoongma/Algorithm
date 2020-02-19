def dfs(v, city):
    visited[v] = True
    for w in G[v]:
        if not visited[w] and w in city:
            path.append(w)
            dfs(w, city)

def subset(N):
    for i in range(1 << N):
        tempA, tempB = [], []
        for j in range(N):
            if i & (1 << j):
                tempA.append(j + 1)
            else:
                tempB.append(j + 1)
        if len(tempA) != 0 and len(tempB) != 0:
            A.append(tempA)
            B.append(tempB)

N = int(input())
num = [0] + list(map(int, input().split()))
G = [[] for _ in range(N + 1)]
min_diff = 0xffffffff

for i in range(1, N + 1):
    temp = list(map(int, input().split()))
    for j in range(temp[0]):
        G[i].append(temp[1 + j])

A, B = [], []
subset(N)
for i in range(len(A)):
    visited = [False for _ in range(N + 1)]
    path = [A[i][0]]
    dfs(A[i][0], A[i])
    if sorted(path) != sorted(A[i]): continue

    visited = [False for _ in range(N + 1)]
    path = [B[i][0]]
    dfs(B[i][0], B[i])
    if sorted(path) != sorted(B[i]): continue

    Asum, Bsum = 0, 0
    for j in range(len(A[i])):
        Asum += num[A[i][j]]
    for j in range(len(B[i])):
        Bsum += num[B[i][j]]

    min_diff = min(min_diff, abs(Asum - Bsum))

if min_diff == 0xffffffff:
    print(-1)
else:
    print(min_diff)
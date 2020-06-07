N = int(input())
adj = [[999 for i in range(N)] for _ in range(N)]

for i in range(N):
    adj[i][i] = 0

while True:
    u, v = map(int, input().split())
    if u == -1 and v == -1: break
    else: adj[u-1][v-1], adj[v-1][u-1] = 1, 1

for k in range(N):
    for i in range(N):
        for j in range(N):
            adj[i][j] = min(adj[i][j], adj[i][k] + adj[k][j])

score = [0] * N
for i in range(N):
    score[i] = max(adj[i])

min_score = 0xffffffff
result, count = [], 0
for i in range(N):
    if score[i] < min_score:
        min_score = score[i]
        result = [i + 1]
        count = 1
    elif score[i] == min_score:
        result.append(i + 1)
        count += 1

print(min_score, count)
print(' '.join(map(str, result)))
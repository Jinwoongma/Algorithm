def dfs(v, color):
    global result
    global max_count
    global count
    if count >= max_count:
        max_count = count
        result += data[v]
    visited[v] = True
    count += 1
    for w in G[v]:
        if w in color and not visited[w]:
            dfs(w, color)

def subset(arr):
    for i in range(1 << N):
        tempA, tempB = [], []
        for j in range(N):
            if i & (1 << j):
                tempA.append(j)
            else:
                tempB.append(j)
        subs.append((tempA, tempB))

N = int(input())
data = list(map(int, input().split()))
G = [[] for _ in range(N)]
subs = []
min_diff = 0xffffffff

# 그래프 생성
for i in range(0, N):
    temp = list(map(int, input().split()))
    for j in range(temp[0]):
        G[i].append(temp[j+1]-1)
# 부분집합 생성
subset(data)

for i in range(len(subs)):
    A, B = [], []
    for j in range(len(subs[i][0])):
        A.append(data[subs[i][0][j]])
    for j in range(len(subs[i][1])):
        B.append(data[subs[i][1][j]])
    Aind, Bind = subs[i][0], subs[i][1]

    if len(A) == 0 or len(B) == 0:
        continue

    visited = [False for _ in range(N + 1)]
    result, max_count, count = 0, 0, 0
    dfs(Aind[0], Aind)
    A_result, A_count = result, max_count

    visited = [False for _ in range(N + 1)]
    result, max_count, count = 0, 0, 0
    dfs(Bind[0], Bind)
    B_result, B_count = result, max_count

    if A_count != len(A)-1 or B_count != len(B)-1:
        continue

    diff = abs(A_result - B_result)
    if diff <= min_diff:
        min_diff = diff

if min_diff == 0xffffffff:
    print(-1)
else:
    print(min_diff)

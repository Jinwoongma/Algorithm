# import sys
# sys.stdin = open('input_1267.txt', 'r')
from collections import deque

for tc in range(1, 11):
    V, E = map(int, input().split())

    G = [[] for i in range(V + 1)]
    in_degree = [0] * (V + 1)

    arr = list(map(int, input().split()))
    for i in range(0, E):
        u, v = arr[i * 2], arr[i * 2 + 1]
        G[u].append(v)  # 유향 그래프
        in_degree[v] += 1

    print(in_degree)
    Q = deque()
    for i in range(1, V + 1):
        if in_degree[i] == 0:
            Q.append(i)

    ans = []
    while len(Q) > 0:
        v = Q.popleft()
        ans.append(v)
        for w in G[v]:
            if in_degree[w] != 0:
                in_degree[w] -= 1
                if in_degree[w] == 0:
                    Q.append(w)

    print("#%d" % tc, end="")
    for val in ans:
        print(" %d" % val, end="")
    print()
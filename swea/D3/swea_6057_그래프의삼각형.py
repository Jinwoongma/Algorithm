import sys
sys.stdin = open('input_6057.txt', 'r')

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    G = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(M):
        v, u = map(int, input().split())
        G[v][u], G[u][v] = 1, 1

    for i in range(N + 1):
        print(G[i])
    print()

    temp = []
    cycle = 0
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                if G[i][j] != 0 and G[i][k] != 0 and G[j][k] != 0:
                    cycle += 1

    print('#{} {}'.format(tc + 1, cycle//6))
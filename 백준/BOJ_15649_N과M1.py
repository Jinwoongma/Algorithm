def combi(index):
    if index == m:
        print(' '.join(map(str, arr)))

    for i in range(n):
        if not visited[i]:
            arr.append(N[i])
            visited[i] = True
            combi(index + 1)
            visited[i] = False
            arr.pop()


n, m = map(int, input().split())
visited = [False for _ in range(n)]
N = list(range(1, n + 1))
arr = []
combi(0)
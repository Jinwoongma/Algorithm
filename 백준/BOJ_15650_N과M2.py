def permutation(index, start):
    if index == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            arr.append(i + 1)
            permutation(index + 1, i + 1)
            visited[i] = False
            arr.pop()


N, M = map(int, input().split())
visited = [False for _ in range(N)]
arr = []
permutation(0, 0)
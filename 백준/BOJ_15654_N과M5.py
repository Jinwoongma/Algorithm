def combi(index):
    if index == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = True
            arr.append(num[i])
            combi(index + 1)
            visited[i] = False
            arr.pop()


N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
arr = []
visited = [False for _ in range(N)]
combi(0)
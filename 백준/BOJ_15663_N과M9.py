def combi(index):
    if index == M:
        print(' '.join(map(str, arr)))
        return

    before = -1
    for i in range(N):
        if visited[i] or num[i] == before: continue
        visited[i] = True
        before = num[i]
        arr.append(num[i])
        combi(index + 1)
        visited[i] = False
        arr.pop()

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [False for _ in range(N)]
check = [False for _ in range(100001)]
arr = []
result = []
combi(0)

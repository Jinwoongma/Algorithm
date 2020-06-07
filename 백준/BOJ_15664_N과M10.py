def combi(index):
    if index == M:
        print(' '.join(map(str, arr)))
        return
    before = -1
    for i in range(N):
        if not visited[i] and num[i] != before:
            if len(arr) == 0:
                arr.append(num[i])
            else:
                if num[i] >= arr[-1]:
                    arr.append(num[i])
                else: continue
            visited[i] = True
            before = num[i]
            combi(index + 1)
            visited[i] = False
            arr.pop()

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
visited = [False for _ in range(N)]
arr = []
combi(0)
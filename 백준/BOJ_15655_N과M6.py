def permutation(index, start):
    if index == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(start, N):
        if not visited[i]:
            if len(arr) == 0:
                arr.append(num[i])
            else:
                if num[i] > arr[-1]:
                    arr.append(num[i])
                else: continue

            visited[i] = True
            permutation(index + 1, i + 1)
            visited[i] = False
            arr.pop()

N, M = map(int, input().split())
num = list(map(int, input().split()))
visited = [False for _ in range(N)]
arr = []
num.sort()
permutation(0, 0)
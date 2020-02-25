def permutation(k):
    if k == M:
        print(' '.join(map(str, order)))
        return

    else:
        before = -1
        for i in range(N):
            if visit[i] == 1 or arr[i] == before:
                continue
            visit[i] = 1
            before = arr[i]
            order.append(arr[i])
            permutation(k+1)
            visit[i] = 0
            order.pop()

N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
visit = [0] * N
order = []
permutation(0)
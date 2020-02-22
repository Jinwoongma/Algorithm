def permutation(index):
    if index == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(N):
        if len(arr) == 0:
            arr.append(i + 1)
        else:
            if i + 1 >= arr[-1]:
                arr.append(i + 1)
            else: continue
        permutation(index + 1)
        arr.pop()

N, M = map(int, input().split())
arr = []
permutation(0)
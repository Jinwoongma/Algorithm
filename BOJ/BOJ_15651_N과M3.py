def permutation(index):
    if index == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(N):
        arr.append(i + 1)
        permutation(index + 1)
        arr.pop()

N, M = map(int, input().split())
arr = []
permutation(0)
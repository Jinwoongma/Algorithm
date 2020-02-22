def combi(index):
    if index == M:
        print(' '.join(map(str, arr)))
        return
    for i in range(N):
        arr.append(num[i])
        combi(index + 1)
        arr.pop()

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
arr = []
combi(0)


def combi(index):
    if index == M:
        print(' '.join(map(str, arr)))
        return

    before = -1
    for i in range(N):
        if num[i] == before: continue
        if len(arr) == 0:
            arr.append(num[i])
        else:
            if num[i] >= arr[-1]:
                arr.append(num[i])
            else: continue
        before = num[i]
        combi(index + 1)
        arr.pop()

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
arr = []
combi(0)
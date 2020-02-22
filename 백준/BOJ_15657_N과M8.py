def combi(index):
    if index == M:
        print(' '.join(map(str, arr)))
        return

    for i in range(N):
        if len(arr) == 0:
            arr.append(num[i])
        else:
            if num[i] >= arr[-1]:
                arr.append(num[i])
            else: continue
        combi(index + 1)
        arr.pop()

N, M = map(int, input().split())
num = sorted(list(map(int, input().split())))
arr = []
combi(0)
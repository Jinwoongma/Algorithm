def calc(arr):
    L = len(arr)
    ret = 0
    for i in range(L - 1):
        for j in range(i, L):
            ret += data[arr[i]][arr[j]] + data[arr[j]][arr[i]]
    return ret


def combi(index, start):
    if index == N // 2:
        result.append(arr[:])
        return
    for i in range(start, N):
        arr.append(i)
        combi(index + 1, i + 1)
        arr.pop()


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
result, arr = [], []
min_diff = 0xffffffff
combi(0, 0)
for i in range(len(result) // 2):
    start = calc(result[i])
    link = calc(result[len(result) - i - 1])
    min_diff = min(min_diff, abs(start - link))
print(min_diff)
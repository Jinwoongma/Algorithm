def solve(arr):
    global answer
    if len(arr) == 1:
        answer = max(answer, arr[0])
        return
    if len(arr) == 0:
        return
    MIN = min(arr)
    index = arr.index(MIN)
    answer = max(answer, len(arr) * MIN)
    left = arr[:index]
    right = arr[index + 1:]
    solve(left)
    solve(right)


N = int(input())
S = []
answer = -1
for i in range(N):
    S.append(int(input()))
solve(S)
print(answer)
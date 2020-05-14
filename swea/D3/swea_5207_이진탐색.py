def solve(arr, val, pre):
    global answer
    # print(lo, hi, (lo + hi) // 2)
    if len(arr) == 0:
        return
    lo, hi = 0, len(arr) - 1
    mid = (lo + hi) // 2
    if arr[mid] == val:
        answer += 1
    elif arr[mid] < val and pre != 1:
        solve(arr[mid + 1:], val, 1)
    elif arr[mid] > val and pre != -1:
        solve(arr[:mid], val, -1)
    return


TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = list(map(int, input().split()))
    answer = 0
    for b in B:
        solve(A, b, 0)
    print('#{} {}'.format(tc + 1, answer))
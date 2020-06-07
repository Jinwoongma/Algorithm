arr = [9, 5, 7, 5, 4, 2, 6, 8]
N = len(arr)


def getMin(lo, hi):  # arr에서 최소값을 찾아서 반환하는 함수
    print(lo, hi)
    if lo == hi: return arr[lo]

    mid = (lo + hi) >> 1
    l = getMin(lo, mid)
    r = getMin(mid + 1, hi)
    return min(l, r)


print(getMin(0, N - 1))
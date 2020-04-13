# Merge Sort는 더이상 나누어지지 않을 때 까지 반 씩(1/2) 분할하다가
# 더 이상 나누어지지 않은 경우(원소가 하나인 배열일 때)에는 자기 자신, 즉 원소 하나를 반환한다.
# 원소가 하나인 경우에는 정렬할 필요가 없기 때문이다. 이 때 반환한 값끼리 combine될 때, 비교가 이뤄지며,
# 비교 결과를 기반으로 정렬되어 임시 배열에 저장된다. 그리고 이 임시 배열에 저장된 순서를 합쳐진 값으로 반환한다.
# 실제 정렬은 나눈 것을 병합하는 과정에서 이뤄지는 것이다.

# 공간복잡도: O(n)
# 시간복잡도: O(nlogn)

# 1.pythonic한 방법
# 슬라이싱을 사용하기 때문에 자료의 개수가 많을때는 비효율적
arr = [69, 10, 30, 2, 16, 8, 31, 22]
def mergeSort(lst):
    # 기저사례
    if len(lst) == 1:
        return lst
    # len(lst) > 1

    mid = len(lst) >> 1 # 중간 위치 설정
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])

    # merge
    ret = []
    while left and right:
        if left[0] < right[0]:
            ret.append(left.pop(0))
        else:
            ret.append(right.pop(0))
    ret.extend(left)
    ret.extend(right)
    return ret

sorted = mergeSort(arr)
print(sorted)

###################################################

# 2. C style
arr= [69, 10, 30, 2, 16, 8, 31, 22]
N = len(arr)
tmp = [0] * N

# 문제의 크기를 범위로 표현
def mergeSort(lo, hi):
    if lo == hi: return

    # division
    mid = (lo + hi) >> 1
    mergeSort(lo, mid)
    mergeSort(mid + 1, hi)

    # merge
    i, j, k = lo, mid + 1, lo
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j]
            j, k = j + 1, k + 1
    while i <= mid:
        tmp[k] = arr[i]
        i, k = i + 1, k + 1
    while j <= hi:
        tmp[k] = arr[j]
        j, k = j + 1, k + 1
    for i in range(lo, hi + 1):
        arr[i] = tmp[i]

mergeSort(0, N - 1)
print(arr)
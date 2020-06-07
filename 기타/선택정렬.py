# n 개의 원소를 가진 배열을 정렬할 때, 계속해서 바꾸는 것이 아니라
# 비교하고 있는 값의 index 를 저장해둔다. 그리고 최종적으로 한 번만 바꿔준다.
# 하지만 여러 번 비교를 하는 것은 마찬가지이다.
# 제자리 정렬이다. (in-place sorting)

# 공간복잡도 O(n)
# 시간복잡도 O(N^2)

arr = [69, 10, 30, 2, 16, 8, 31, 22]

for i in range(len(arr) - 1): # 바꿀 위치
    # 최소값의 인덱스를 찾는다
    minIdx = i
    for j in range(i + 1, len(arr)):
        if arr[minIdx] > arr[j]:
            minIdx = j
    arr[i], arr[minIdx] = arr[minIdx], arr[i]

print(arr)
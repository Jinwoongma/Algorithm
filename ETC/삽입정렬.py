# n 개의 원소를 가진 배열을 정렬할 때, i 번째를 정렬할 순서라고 가정하면, 0 부터 i-1 까지의 원소들은
# 정렬되어있다는 가정하에, i 번째 원소와 i-1 번째 원소부터 0 번째 원소까지 비교하면서 i번째 원소가
# 비교하는 원소보다 클 경우 서로의 위치를 바꾸고, 작을 경우 위치를 바꾸지 않고 다음 순서의 원소와 비교하면서 정렬해준다.
# 이 과정을 정렬하려는 배열의 마지막 원소까지 반복해준다.
# 제자리 정렬이다(in-place sorting)
# 대부분의 원소가 정렬이 되어있는 경우 효율적이다.
# 같은 O(N^2) 알고리즘들보다 상대적으로 빠르다

# 공간복잡도 O(1)
# 시간복잡도 O(N^2), 최선의 경우 O(N)
arr = [69, 10, 30, 2, 16, 8, 31, 22]
for i in range(1, len(arr)):
    tmp = arr[i]
    j = i - 1
    while j >= 0 and arr[j] > tmp:
        arr[j + 1] = arr[j]
        j -= 1
    arr[j + 1] = tmp

print(arr)
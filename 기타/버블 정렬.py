# Bubble Sort는 Selection Sort와 유사한 알고리즘으로
# 서로 인접한 두 원소의 대소를 비교하고, 조건에 맞지 않다면
# 자리를 교환하며 정렬하는 알고리즘 이다.

# 시간복잡도 O(N^2)
# 공간복잡도 O(n)

arr = [69, 10, 30, 2, 16, 8, 31, 22]
L = len(arr)
for i in range(L):
    for j in range(1, L - i):
        if arr[j - 1] > arr[j]:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]

print(arr)
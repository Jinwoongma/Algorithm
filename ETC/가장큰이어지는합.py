# 정수 배열(int array)가 주어지면 가장 큰 이어지는 원소들의 합을 구하시오. 단, 시간복잡도는 O(n).
# Given an integer array, find the largest consecutive sum of elements.
# Input: [-1, 3, -1, 5]
# Output: 7 // 3 + (-1) + 5

nums = list(map(int, input().split()))
D = [-1 for _ in range(len(nums))]
D[0] = nums[0]
for i in range(1, len(nums)):
    D[i] = max(D[i - 1] + nums[i], nums[i])
print(D[len(nums) - 1])
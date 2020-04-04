from itertools import permutations
nums = sorted(list(map(int, input().split())))
K = int(input())

for idx, perms in enumerate(permutations(nums)):
    if idx == K - 1:
        print(' '.join(map(str, list(perms))))

###############################################

# nums = sorted(list(map(int, input().split())))
# K = int(input())
# arr = [[0 for _ in range(10)] for _ in range(10)]
# arr[0][0] = nums[0]; arr[0][1] = nums[1]; arr[0][2] = nums[2]
# arr[1][0] = nums[0]; arr[1][1] = nums[2]; arr[1][2] = nums[1]
# arr[2][0] = nums[1]; arr[2][1] = nums[0]; arr[2][2] = nums[2]
# arr[3][0] = nums[1]; arr[3][1] = nums[2]; arr[3][2] = nums[0]
# arr[4][0] = nums[2]; arr[4][1] = nums[0]; arr[4][2] = nums[1]
# arr[5][0] = nums[2]; arr[5][1] = nums[1]; arr[5][2] = nums[0]
#
# for i in range(3):
#     print(arr[K - 1][i])

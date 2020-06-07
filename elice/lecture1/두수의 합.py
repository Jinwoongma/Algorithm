
def twoSum(nums, target):
    nums.sort()
    s, e = 0, len(nums) - 1
    while True:
        if nums[s] + nums[e] > target:
            e -= 1
        elif nums[s] + nums[e] < target:
            s += 1
        elif nums[s] + nums[e] == target:
            return nums[s], nums[e]


def main():
    print(twoSum([2, 8, 19, 37, 4, 5], 12)) # (4, 8) 혹은 (8, 4)가 리턴되어야 합니다.

if __name__ == "__main__":
    main()

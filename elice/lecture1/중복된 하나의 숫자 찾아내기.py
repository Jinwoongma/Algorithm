def findDuplicate(nums):
    n = len(nums)
    check = [False] * (n + 1)
    for i in range(n):
        if not check[nums[i] + 1]:
            check[nums[i] + 1] = True
        else:
            return nums[i]

def main():
    print(findDuplicate([1, 5, 2, 4, 5, 6, 3]))

if __name__ == "__main__":
    main()
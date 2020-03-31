# 공간복잡도 O(1)로 풀기
def moveZerosToEnd(nums):
    currentPosition = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[currentPosition] = nums[i]
            nums[i] = 0
            currentPosition += 1
    return nums


def main():
    print(moveZerosToEnd([0, 8, 0, 37, 4, 5, 0, 50, 0, 34, 0, 0]))


if __name__ == "__main__":
    main()

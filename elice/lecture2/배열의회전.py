# 이 함수를 수정 해 주세요.
def rotateArray(nums, k):
    return nums[-1 * k:] + nums[:len(nums) - k]


# 다음 함수는 추가적인 공간 사용 없이 배열의 일부를 뒤집어 주는 함수입니다.
# 예를 들어, nums = [1,2,3,4,5]
# partialReverse(nums, 1, 3)
# 을 실행 할 경우, nums = [1, 4, 3, 2, 5] 가 됩니다.
# 필요하다면 사용하세요.
def partialReverse(nums, start, end):
    for i in range(0, int((end - start) / 2) + 1):
        temp = nums[start + i]
        nums[start + i] = nums[end - i]
        nums[end - i] = temp


def main():
    nums = [1, 2, 3, 4, 5]
    partialReverse(nums, 1, 3)  # [1, 4, 3, 2, 5] 를 반환합니다.
    print(rotateArray([1, 2, 3, 4, 5, 6, 7, 8, 9], 8))  # [6,7,8,9,1,2,3,4,5] 를 반환해야 합니다.


if __name__ == "__main__":
    main()

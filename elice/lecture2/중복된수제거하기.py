
def removeDuplicate(nums):
    ret = []
    ref = -1
    for i in range(len(nums)):
        if nums[i] != ref:
            ref = nums[i]
            ret.append(nums[i])
    return ret

def main():
    print(removeDuplicate([1, 1, 2, 2, 2, 2, 5, 7, 7, 8])) # [1, 2, 5, 7, 8]을 리턴해야 합니다

if __name__ == "__main__":
    main()
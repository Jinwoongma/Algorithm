from collections import deque


def josephus(num, target):
    ret = []
    nums = list(range(1, num + 1))
    cnt = 1
    idx = 0
    while True:
        if len(nums) == 0:
            break
        if idx >= len(nums):
            idx = 0
        if cnt == target:
            cnt = 1
            ret.append(nums[idx])
            nums = nums[:idx] + nums[idx + 1:]
        else:
            cnt += 1
            idx += 1

    return ret


def main():
    print(josephus(7, 3))  # [3, 6, 2, 7, 5, 1, 4]이 반환되어야 합니다


if __name__ == "__main__":
    main()
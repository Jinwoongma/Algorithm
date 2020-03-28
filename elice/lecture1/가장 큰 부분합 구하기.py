def maxSubArray(nums):
    N = len(nums)
    nums = [0] + nums
    dp = [-0xffffff for _ in range(N + 1)]
    dp[0] = 0
    for i in range(1, N + 1):
        dp[i] = max(0, dp[i - 1]) + nums[i]

    return max(dp)


def main():
    print(maxSubArray([-10, -7, 5, -7, 10, 5, -2, 17, -25, 1]))  # 30이 리턴되어야 합니다


if __name__ == "__main__":
    main()
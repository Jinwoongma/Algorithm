import sys
sys.stdin = open('input_3307.txt', 'r')

TC = int(input())
for tc in range(TC):
    N = int(input())
    data = list(map(int, input().split()))
    dp = [0] * (N + 1)
    # dp[0] = 1
    # for i in range(1, N):
    #     dp[i] = 1
    #     for j in range(N):
    #         if data[i] > data[j] and dp[j] + 1 > dp[i]:
    #             dp[i] = dp[j] + 1
    # print(dp)

    for i in range(N):
        if dp[i] == 0:
            dp[i] = 1
        for j in range(i):
            if data[i] > data[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    print('#{} {}'.format(tc + 1, max(dp)))
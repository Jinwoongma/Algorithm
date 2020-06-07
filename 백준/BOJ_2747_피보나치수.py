def fibo(ind):
    if dp[ind] == -1:
        dp[ind] = fibo(ind - 2) + fibo(ind - 1)
    return dp[ind]

N = int(input())
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    dp = [-1] * (N + 1)
    dp[0], dp[1] = 0, 1
    print(fibo(N))
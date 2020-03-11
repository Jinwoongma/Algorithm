def solve(idx, c):
    if idx <= 0:
        return 0

    if dp[c][idx] != -1:
        return dp[c][idx]

    dp[c][idx] = stair[idx]
    if c == 0:
        ret = max(solve(idx - 1, 1), solve(idx - 2, 0))
    elif c == 1:
        ret = solve(idx - 2, 0)
    dp[c][idx] += ret

    return dp[c][idx]

N = int(input())
stair = [0]
for i in range(1, N + 1):
    stair.append(int(input()))
dp = [[-1 for _ in range(N + 1)] for _ in range(3)]
print(solve(N, 0))
# print(dp)

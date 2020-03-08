import sys
sys.setrecursionlimit(100000)
def solve(tot, late, abs):
    if late >= 2 or abs >= 3:
        return 0

    if tot == N:
        return 1

    if (tot, late, abs) in memo:
        return memo[(tot, late, abs)]

    memo[(tot, late, abs)] = (solve(tot + 1, late, 0) + solve(tot + 1, late + 1, 0) + solve(tot + 1, late, abs + 1))
    return memo[(tot, late, abs)]


N = int(input())
dp = [[[-1 for _ in range(4)] for _ in range(3)] for _ in range(N + 1)]
memo = {}
print(solve(0, 0, 0) % 1000000)

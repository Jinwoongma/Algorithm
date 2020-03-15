import sys
sys.setrecursionlimit(1000000)

def solve(y, x, length):
    global cnt
    if y == R and x == C:
        print(cnt)
        sys.exit(0)

    if length == 1:
        cnt += 1
        return 0

    if R >= y + length:
        cnt += length**2
        return 0

    if C >= x + length:
        cnt += length**2
        return 0

    solve(y, x, length // 2)
    solve(y, x + length // 2, length // 2)
    solve(y + length // 2, x, length // 2)
    solve(y + length // 2, x + length // 2, length // 2)


N, R, C = map(int, input().split())
cnt = 0
solve(0, 0, 2**N)
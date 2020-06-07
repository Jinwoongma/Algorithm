
def solve(n, y, x):
    if n == 1:
        data[y][x] = '*'
    else:
        for i in range(3):
            for j in range(3):
                if i != 1 or j != 1:
                    solve(n//3, y + (n//3) * i, x + (n//3) * j)


N = int(input())
data = [[' ' for _ in range(N)] for _ in range(N)]
solve(N, 0, 0)
for i in data:
    print(*i, sep='')
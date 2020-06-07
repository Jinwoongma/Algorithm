N = int(input())
MAP = [list(map(int, input().strip())) for _ in range(2 ** N)]
result = ''

def solve(n, y, x):
    global result
    if n == 1:
        result += str(MAP[y][x])
        return

    flag = True
    for i in range(y, y + n):
        if not flag:
            break
        for j in range(x, x + n):
            if MAP[i][j] != MAP[y][x]:
                flag = False
                break

    if flag:
        result += str(MAP[y][x])
    else:
        decreased_n = n // 2

        result += 'x'
        solve(decreased_n, y, x)
        solve(decreased_n, y, x + decreased_n)
        solve(decreased_n, y + decreased_n, x)
        solve(decreased_n, y + decreased_n, x + decreased_n)


solve(2 ** N, 0, 0)
print(result)
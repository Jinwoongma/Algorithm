def solve(pos, value):
    if pos == N: return 0
    unselected = solve(pos + 1, value)
    selected = 0
    if value >= data[pos][1]:
        selected = solve(pos + 1, value - data[pos][1]) + data[pos][0]
    return max(unselected, selected)


TC = int(input())
for tc in range(TC):
    N, L = map(int, input().split())
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))

    print('#{} {}'.format(tc + 1, solve(0, L)))
def dfs(month, price):
    global min_price
    if month >= 12:
        min_price = min(min_price, price)
        return

    if m[month] == 0:
        dfs(month + 1, price)
    else:
        dfs(month + 1, price + p[0] * m[month])
        dfs(month + 1, price + p[1])
        dfs(month + 3, price + p[2])


TC = int(input())
for tc in range(TC):
    p = list(map(int, input().split()))
    m = list(map(int, input().split()))
    check = [0] * 12
    min_price = p[3]
    dfs(0, 0)
    print('#{} {}'.format(tc + 1, min_price))
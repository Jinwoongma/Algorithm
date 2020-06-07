def service_area(k):
    n = k * 2 - 1
    area = [[0 for _ in range(n)] for _ in range(n)]
    blank, fill = k - 1, 1
    for i in range(k):
        for j in range(n):
            if blank <= j < blank + fill:
                area[i][j] = 1
        blank -= 1
        fill += 2

    blank, fill = 1, k * 2 - 3
    for i in range(k, n):
        for j in range(n):
            if blank <= j < blank + fill:
                area[i][j] = 1
        blank += 1
        fill -= 2
    return area

def padding(MAP, k):
    n = k * 2 - 1
    m = len(MAP)
    new_MAP = []
    for i in range(m + (2 * n) - 2):
        if i < n - 1 or i >= m + (n - 1):
            new_MAP.append([0] * (m + (2 * n) - 2))
        else:
            temp = MAP[i - (n - 1)]
            temp = [0] * (n - 1) + temp + [0] * (n - 1)
            new_MAP.append(temp)
    # for i in range(m + (2 * n) - 2):
    #     print(new_MAP[i])
    # print()
    return new_MAP


TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    temp = 0
    for k in range(1, N + 2):
        cost = (k * k) + ((k - 1) * (k - 1))
        area = service_area(k)
        new_MAP = padding(MAP, k)

        for sy in range(N + (k * 2 - 1) - 1):
            for sx in range(N + (k * 2 - 1) - 1):
                get = 0
                for r in range(k * 2 - 1):
                    for c in range(k * 2 - 1):
                        if area[r][c] and new_MAP[sy + r][sx + c]:
                            get += M

                if get - cost >= 0:
                    if get // M > result:
                        result = get // M

    print('#{} {}'.format(tc + 1, result))

TC = int(input())
for tc in range(TC):
    N = int(input())
    data = []
    for i in range(N):
        s, e = map(int, input().split())
        data.append([s, e])
    data.sort(key=lambda x: x[1])

    T = data[0][1]
    ans = 1
    for i in range(1, len(data)):
        s, e = data[i]
        if s >= T:
            ans += 1
            T = e
    print('#{} {}'.format(tc + 1, ans))
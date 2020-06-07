def get_gcd(a, b):
    while b != 0:
        n = a % b
        a, b = b, n
    return a

TC = int(input())
for tc in range(TC):
    M, N, X, Y = map(int, input().split())

    if M > N:
        gcd = get_gcd(M, N)
    else:
        gcd = get_gcd(M, N)
    max_year = gcd * (M // gcd) * (N // gcd)

    index = 0
    flag = False
    while True:
        year = X + (M * index)
        if year > max_year:
            print(-1)
            flag = True
            break

        if year % N != 0:
            ty = year % N
        else:
            ty = N

        if ty == Y:
            print(year)
            flag = True
            break
        index += 1
def solve(num, check):
    if num == 1:
        return 0

    if check[num] != -1:
        return check[num]

    ret = 0xfffff
    if not num % 2:
        ret = 1 + solve(num // 2, check)
    if not num % 3:
        ret = min(ret, 1 + solve(num // 3, check))
    if num % 6:
        ret = min(ret, 1 + solve(num - 1, check))

    check[num] = ret
    return check[num]


def convertTo1(num):
    check = [-1] * (num + 1)
    return solve(num, check)


def main():
    print(convertTo1(10))


if __name__ == "__main__":
    main()

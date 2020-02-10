def combination(k, s):
    global count
    global pick
    if k == r:
        count += 1
        # for i in range(r):
        #     print(pick[i], end=' ')
        # print()
    elif s <= (n//2) and k < r:
        return
    else:
        for i in range(s, n+1):
            if k == 0:
                pick[k] = i
                combination(k + 1, i + 1)
            else:
                if i >= pick[k-1] * 2:
                    pick[k] = i
                    combination(k + 1, i + 1)
                else:
                    continue


TC = int(input())
for tc in range(TC):
    r, n = map(int, input().split())
    pick = [0] * r
    count = 0
    combination(0, 1)
    print(count)

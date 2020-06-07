K = int(input())
data = list(map(int, input().split()))
ans = -1
before_zero = False
for i in range(K):
    if data[i] == 0:
        if not before_zero:
            before_zero = True
            l_MIN, r_MIN = 0xfffff, 0xfffff
            MIN = 0xfffff
            j = 0
            while True:
                li = i - j
                if 0 <= li < K:
                    if data[li] == 1:
                        l_MIN = min(MIN, j)
                        break
                else: break
                j += 1

            j = 0
            while True:
                ri = i + j
                if 0 <= ri < K:
                    if data[ri] == 1:
                        r_MIN = min(MIN, j)
                        break
                else: break
                j += 1
        else:
            l_MIN += 1
            r_MIN -= 1
        MIN = min(l_MIN, r_MIN)
        ans = max(ans, MIN)
    elif data[i] == 1:
        before_zero = False

print(ans)
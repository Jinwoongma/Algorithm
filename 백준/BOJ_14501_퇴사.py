N = int(input())
T = [0] * (N + 1)
P = [0] * (N + 1)


for i in range(1, N + 1):
    t, p = map(int, input().split())
    T[i], P[i] = t, p

for k in range(1, N + 1):
    vlaue = [0] * (N + 1)

    remain = N
    for i in range(k, N + 1):
        while True:
            if remain - T[i] > 0:
                for j in range(T[i]):
                    vlaue[i + j] = P[i]
                remain -= T[i]
                break
            else: break
        print(sum(set(vlaue)))
    print()

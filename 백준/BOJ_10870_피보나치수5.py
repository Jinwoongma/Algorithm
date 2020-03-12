def fibo(idx):
    if idx < 0:
        return 0
    if d[idx] != -1:
        return d[idx]
    d[idx] = fibo(idx - 2) + fibo(idx - 1)
    return d[idx]


N = int(input())
d = [-1 for _ in range(30)]
d[0], d[1] = 0, 1
print(fibo(N))
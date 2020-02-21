def fatorial(n):
    if n == 0:
        return 1
    if n < 2:
        return n
    return n * fatorial(n-1)

N = int(input())
print(fatorial(N))
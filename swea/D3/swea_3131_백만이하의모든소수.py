n = 1000000
check = [False, False] + [True] * (n - 1)  # 0과 1 제거
primes = []

for i in range(2, int(n**0.5)):
    if check[i]:
        for j in range(i * i, n+1, i):
            check[j] = False

primes = [i for i in range(n + 1) if check[i]]
print(' '.join(map(str, primes)))

#
# n = 1000000
# check = [False, False] + [True] * (n - 1)  # 0과 1 제거
# primes = []
#
# for i in range(2, n + 1):
#     if check[i]:
#         primes.append(i)
#     for j in range(2 * i, n+1, i):
#         check[j] = False
# print(' '.join(map(str, primes)))
num = int(input())
N = len(str(num))
result = 0

for i in range(1, N + 1):
    temp = 10 ** i
    if i != N:
        result += (i * ((10 ** i) - (10 ** (i - 1))))
    elif i == N:
        result += (i * (num - (10 ** (i - 1)) + 1))

print(result)
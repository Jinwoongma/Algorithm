N = int(input())
A = sorted(list(map(int, input().split())))
B = list(map(int, input().split()))
new_B = sorted(B, reverse=True)

result = 0
for i in range(N):
    result += (A[i] * new_B[i])
print(result)
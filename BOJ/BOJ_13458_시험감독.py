import math
N = int(input())
data = list(map(int, input().split()))
main, sub = map(int, input().split())
result = N
for i in range(N):
    if data[i] <= main: continue
    else:
        result += math.ceil((data[i] - main) / sub)
print(result)

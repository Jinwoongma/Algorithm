TC = int(input())
for tc in range(TC):
    N = int(input())
    result = 0
    for n in range(N):
        p, x = map(float, input().split())
        result += p * x
    print('#%d %6f' %(tc + 1, result))
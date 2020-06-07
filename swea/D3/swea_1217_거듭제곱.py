import sys
sys.stdin = open('input_1217.txt', 'r')

def cal(n, cnt):
    if cnt == M:
        return n
    else:
        return cal(n * N, cnt + 1)

for tc in range(10):
    t = int(input())
    N, M = map(int, input().split())
    result = 1
    print('#{} {}'.format(tc + 1, cal(N, 1)))
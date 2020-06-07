import sys
sys.stdin = open('input.txt', 'r')

def calc(index, result):
    global max_result
    if index == N:
        max_result = result
        return

    for i in range(N):
        if not visited[i]:
            if P[index][i] == 0: continue
            if result * (P[index][i]/100) <= max_result: continue
            visited[i] = True
            calc(index + 1, result * (P[index][i]/100))
            visited[i] = False


TC = int(input())
for tc in range(TC):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    max_result = -1
    calc(0, 1)
    print('#%d %6f'%(tc + 1, max_result * 100))
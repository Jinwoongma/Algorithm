import sys
sys.stdin = open('input.txt', 'r')

def dfs(index, arr, s):
    global max_sum, min_sum
    if index == N - 1:
        ret = calc(arr)
        max_sum = max(max_sum, ret)
        min_sum = min(min_sum, ret)
        return
    for i in range(4):
        if s[i] == 0: continue
        s[i] -= 1
        arr += sign[i]
        dfs(index + 1, arr, s)
        s[i] += 1
        arr.pop()


def calc(arr):
    result = num[0]
    for i in range(N - 1):
        if arr[i] == '+':
            result += num[i + 1]
        elif arr[i] == '-':
            result -= num[i + 1]
        elif arr[i] == '*':
            result *= num[i + 1]
        else:
            if result == 0:
                result = 0
            else:
                if result > 0:
                    result = result // num[i + 1]
                else:
                    result = -1 * (-1 * result // num[i + 1])
    return result


TC = int(input())
for tc in range(TC):
    N = int(input())
    s = list(map(int, input().split()))
    num = list(map(int, input().split()))
    sign = ['+', '-', '*', '/']
    min_sum, max_sum = 10**8, -1 * (10**8)
    dfs(0, [], s)
    print('#{} {}'.format(tc + 1, max_sum - min_sum))
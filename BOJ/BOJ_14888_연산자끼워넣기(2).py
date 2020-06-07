# 00:24~01:30

def calc(nums, signs):
    L = len(signs)
    ret = nums[0]
    for i in range(L):
        if signs[i] == '+':
            ret += nums[i + 1]
        elif signs[i] == '-':
            ret -= nums[i + 1]
        elif signs[i] == '*':
            ret *= nums[i + 1]
        elif signs[i] == '/':
            if ret < 0 :
                ret = -1 * ((-1 * ret) // nums[i + 1])
            else:
                ret = ret // nums[i + 1]
    return ret


def permutation(idx, n):
    if idx == n:
        memo.add(''.join(ret))
        return
    for i in range(n):
        if not visited[i]:
            ret[idx] = sign[i]
            visited[i] = True
            permutation(idx + 1, n)
            visited[i] = False

N = int(input())
nums = list(map(int, input().split()))
data = list(map(int, input().split()))
sign = ['+'] * data[0] + ['-'] * data[1] + ['*'] * data[2] + ['/'] * data[3]
visited = [False] * len(sign)
memo = set()
ret = [0] * (N - 1)
permutation(0, len(sign))

MAX, MIN = -9**10, 9**10
for i in memo:
    ret = calc(nums, i)
    MAX = max(MAX, ret)
    MIN = min(MIN, ret)
print(MAX)
print(MIN)

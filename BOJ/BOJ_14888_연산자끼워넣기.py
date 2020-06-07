def calc(operator, num):
    L = len(operator)
    result = num[0]
    for i in range(L):
        if operator[i] == '+': result += num[i + 1]
        elif operator[i] == '-': result -= num[i + 1]
        elif operator[i] == '*': result *= num[i + 1]
        else:
            if result < 0:
                result = -1 * ((-1 * result) // num[i + 1])
            else:
                result = result // num[i + 1]
    return result


def permutation(index, cnt):
    global max_result
    global min_result
    if cnt == N - 1:
        result = calc(operator, num)
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    for i in range(index, N-1):
        operator[i], operator[index] = operator[index], operator[i]
        permutation(index + 1, cnt + 1)
        operator[i], operator[index] = operator[index], operator[i]

N = int(input())
num = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
operator = ['+'] * add + ['-'] * sub + ['*'] * mul + ['%'] * div
min_result, max_result = 10**9, -1*(10**9)
permutation(0, 0)

print(max_result)
print(min_result)
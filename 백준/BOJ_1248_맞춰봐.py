# def check(index):
#     global flag
#     sum = 0
#     for i in range(index, -1, -1):
#         sum += arr[i]
#         if assign[i][index] == -1:
#             if sum >= 0: return False
#         elif assign[i][index] == 1:
#             if sum <= 0: return False
#         elif assign[i][index] == 0:
#             if sum != 0: return False
#     return True
#
#
# def solve(index):
#     if index == N:
#         return True
#     if assign[index][index] == 0:
#         arr[index] = 0
#         return solve(index + 1) and check(index)
#     for i in range(1, 11):
#         arr[index] = i * assign[index][index]
#         if solve(index + 1) and check(index):
#             return True
#     return False
#
#
# N = int(input())
# a = input()
# assign = []
# pann, temp = 0, 0
# for i in range(N):
#     temp_arr = []
#     for j in range(pann):
#         temp_arr.append('.')
#     for j in range(N - pann):
#         if a[temp + j] == '-':
#             temp_arr.append(-1)
#         elif a[temp + j] == '+':
#             temp_arr.append(1)
#         elif a[temp + j] == '0':
#             temp_arr.append(0)
#     assign.append(temp_arr)
#     temp += (N - pann)
#     pann += 1
#
# flag = False
# arr = [0] * N
# solve(0)
# print(' '.join(map(str, arr)))

n = int(input())
a = [[0] * n for _ in range(n)]
b = list(map(str, input().strip()))
v, k = [], 0

def possible(idx):
    s = 0
    for i in range(idx, -1, -1):
        s += v[i]
        if a[i][idx] == '+' and s <= 0:
            return False
        if a[i][idx] == '0' and s != 0:
            return False
        if a[i][idx] == '-' and s >= 0:
            return False
    return True

def solve(idx):
    if idx == n:
        print(' '.join(map(str, v)))
        exit(0)
    for i in range(-10, 11):
        v.append(i)
        if possible(idx):
            solve(idx+1)
        v.pop()

for i in range(n):
    for j in range(i, n):
        a[i][j] = b[k]
        k += 1
solve(0)
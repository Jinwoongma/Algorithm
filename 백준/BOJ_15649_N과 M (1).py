# def rotateR(start, end):
#     tmp = nums[end]
#     for i in range(end, start - 1, -1):
#         nums[i] = nums[i - 1]
#     nums[start] = tmp
#
# def rotateL(start, end):
#     tmp = nums[start]
#     for i in range(start, end):
#         nums[i] = nums[i + 1]
#     nums[end] = tmp
#
# def perm(depth):
#     if depth == M:
#         # print(nums)
#         results.append(nums[:M])
#     else:
#         for i in range(depth, N):
#             rotateR(depth, i)
#             perm(depth + 1)
#             rotateL(depth, i)
#
# N, M = map(int, input().split())
# nums = list(range(1, N + 1))
# results = []
# perm(0)
# for result in results:
#     for i in range(M):
#         if i != M-1:
#             print(result[i], end=' ')
#         else:
#             print(result[i], end='')
#     print()

n, m = map(int, input().split())  # 1~n까지 중 m개를 고른 수열
visited = [False] * n
result = []

def dfs(start, depth):
    if depth == m:
        print(*result)
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        result.append(i + 1)
        dfs(start + 1, depth + 1)
        result.pop()
        visited[i] = False

dfs(0, 0)
def dfs(index, SUM):
    S.add(SUM)
    if index == N:
        return
    dfs(index + 1, SUM)
    dfs(index + 1, SUM + nums[index + 1])

TC = int(input())
for tc in range(TC):
    N = int(input())
    nums = list(map(int, input().split()))
    visited = [False for _ in range(10001)]
    visited[0] = True
    ans = 0

    MAX = 0
    for i in range(N):
        MAX += nums[i]
        for j in range(MAX, -1, -1):
            if visited[j]:
                visited[j + nums[i]] = True

    for i in range(10001):
        if visited[i]:
            ans += 1
    print('#{} {}'.format(tc + 1, ans))
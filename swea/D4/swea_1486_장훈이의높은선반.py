def dfs(s, hsum):
    global min_diff
    if hsum >= B:
        min_diff = min(min_diff, hsum - B)
        return
    for i in range(s, N):
        if not visited[i]:
            visited[i] = True
            hsum += h[i]
            dfs(i, hsum)
            hsum -= h[i]
            visited[i] = False

TC = int(input())
for tc in range(TC):
    N, B = map(int, input().split())
    h = list(map(int, input().split()))
    visited = [False for _ in range(N)]
    min_diff = 0xffffffff
    dfs(0, 0)
    print('#{} {}'.format(tc + 1, min_diff))
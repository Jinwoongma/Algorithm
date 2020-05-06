def solve(index):
    global answer, arr
    if index == len(num):
        temp = [0] + arr + [0]
        SUM = 0
        for i in range(len(temp) - 1):
            SUM += MAP[temp[i]][temp[i + 1]]
        answer = min(answer, SUM)
        return
    for i in range(len(num)):
        if not visited[num[i]]:
            arr.append(num[i])
            visited[num[i]] = True
            solve(index + 1)
            arr.pop()
            visited[num[i]] = False

TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    num = range(1, N)
    visited = [False for _ in range(N)]
    arr = []
    answer = 0xfffff
    solve(0)
    print('#{} {}'.format(tc + 1, answer))
def cal(index):
    global min_result
    global result

    if min_result < result:
        return

    if index == N:
        min_result = min(min_result, result)
        return

    for i in range(N):
        if visited[i]: continue
        result += data[index][i]
        visited[i] = True
        cal(index + 1)
        visited[i] = False
        result -= data[index][i]

TC = int(input())
for tc in range(TC):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    min_result, sub_result = 0xffffffff, 0
    cal(0)
    print('#{} {}'.format(tc + 1, min_result))

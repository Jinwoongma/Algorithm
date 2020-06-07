def solve(y, x, index, distance):
    global answer
    if distance >= answer:
        return
    if index == N:
        distance += (abs(y - ey) + abs(x - ex))
        answer = min(answer, distance)
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            solve(home[i][1], home[i][0], index + 1, distance + abs(y - home[i][1]) + abs(x - home[i][0]))
            visited[i] = False


TC = int(input())
for tc in range(TC):
    N = int(input())
    cor = list(map(int, input().split()))
    sx, sy, ex, ey = cor[0], cor[1], cor[2], cor[3]
    home = []
    for i in range(4, len(cor), 2):
        home.append((cor[i], cor[i + 1]))

    visited = [False for _ in range(N)]
    answer = 0xffffff
    solve(sy, sx, 0, 0)
    print('#{} {}'.format(tc + 1, answer))

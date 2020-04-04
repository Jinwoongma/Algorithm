def dfs(y, x):
    global area, value
    visited[y][x] = True  # 해당 좌표 방문 체크
    for dir in range(8):  # 8방향 탐색
        ty, tx = y + dy[dir], x + dx[dir]  # 새로운 좌표 ty, tx
        if ty < 0 or ty >= N or tx < 0 or tx >= N: continue  # 배열의 범위 밖이면 continue
        if not visited[ty][tx] and MAP[ty][tx] == MAP[y][x]:  # 새로운 좌표가 방문된 적이 없고 매장량이 같다면
            area += 1               # 면적 += 1
            value += MAP[ty][tx]    # 매장량 += MAP[ty][tx]
            dfs(ty, tx)             # 새로운 좌표로 탐색


TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    dy = [1, 1, 1, 0, -1, -1, -1, 0]  # 8방향 탐색을 위한 y좌표 delta 값
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]  # 8방향 탐색을 위한 x좌표 delta 값
    visited = [[False for _ in range(N)] for _ in range(N)]  # 방문 체크 배열
    result_area, result_value = -1, -1  # 최대 면적, 최대 매장량

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:  # 탐색한 적이 없을 때
                area, value = 1, MAP[i][j]           # 면적 초기값은 1, 매장량 초기값은 MAP[i][j]
                dfs(i, j)                            # dfs 시작
                if value > result_value:             # i, j 에서의 매장량값이 현재 최대 매장량보다 크다면
                    result_value = value             # 최대 매장량 update
                    result_area = area               # 최대 면적 update
                elif value == result_value:                 # 매장량이 같은 경우에는
                    result_area = min(area, result_area)    # 더 작은 면적으로 update

    print('#{} {} {}'.format(tc + 1, result_value, result_area))
def change(y, x, d, type, path):
    for dir in range(len(delta[type][0])):
        ty, tx = y, x
        while True:
            ty += d[dir][0]
            tx += d[dir][1]
            if ty < 0 or ty >= R or tx < 0 or tx >= C or MAP[ty][tx] == 6:
                break
            if MAP[ty][tx] == 0:
                MAP[ty][tx] = '#'
                path.append([ty, tx])


def solve(index):
    global answer
    if index == len(cameras):
        # 빈칸 계산 후 정답 갱신
        cnt = 0
        for r in range(R):
            for c in range(C):
                if MAP[r][c] == 0:
                    cnt += 1
        answer = min(answer, cnt)
        return
    sy, sx, type = cameras[index]
    for dir in range(len(delta[type])):
        path = []
        change(sy, sx, delta[type][dir], type, path)
        solve(index + 1)
        for y, x in path:
            MAP[y][x] = 0


TC = int(input())
for tc in range(TC):
    R, C = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(R)]
    cameras = []
    delta = [
        [],
        [[(0, 1)], [(1, 0)], [(0, -1)], [(-1, 0)]],
        [[(0, 1), (0, -1)], [(1, 0), (-1, 0)]],
        [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
        [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
        [[(0, -1), (0, 1), (1, 0), (-1, 0)]]
    ]

    for i in range(R):
        for j in range(C):
            if 1 <= MAP[i][j] <= 5:
                cameras.append([i, j, MAP[i][j]])  # y, x, type
    answer = 0xfffff
    solve(0)
    print('#{} {}'.format(tc + 1, answer))
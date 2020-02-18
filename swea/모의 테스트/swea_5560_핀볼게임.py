 # 20:10 ~ 21:04
def change(dir, shape):
    if shape == 1:
        if dir == 0: return 3
        elif dir == 1: return 0
        elif dir == 2: return 1
        else: return 2
    elif shape == 2:
        if dir == 0: return 1
        elif dir == 1: return 3
        elif dir == 2: return 0
        else: return 2
    elif shape == 3:
        if dir == 0: return 1
        elif dir == 1: return 2
        elif dir == 2: return 3
        else: return 0
    elif shape == 4:
        if dir == 0: return 2
        elif dir == 1: return 0
        elif dir == 2: return 3
        else: return 1
    elif shape == 5:
        if dir == 0: return 1
        elif dir == 1: return 0
        elif dir == 2: return 3
        else: return 2


TC = int(input())
for tc in range(TC):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    dy = [1, -1, 0, 0]; dx = [0, 0, -1, 1]  # 상, 하, 좌, 우
    hall = [[] for _ in range(11)]

    # 웜홀 구간 저장
    for i in range(N):
        for j in range(N):
            if 6 <= data[i][j] <= 10:
                hall[data[i][j]].append([i, j])

    max_cnt = -1
    for i in range(N):
        for j in range(N):
            if data[i][j] == 0:
                for k in range(4):
                    cnt, ty, tx, dir = 0, i, j, k
                    while True:
                        ty, tx = ty + dy[dir], tx + dx[dir]

                        # 벽에 부딪혔을 때
                        if ty < 0 and dir == 1:
                            dir = 0; cnt += 1
                            continue
                        elif ty >= N and dir == 0:
                            dir = 1; cnt += 1
                            continue
                        elif tx < 0 and dir == 2:
                            dir = 3; cnt += 1
                            continue
                        elif tx >= N and dir == 3:
                            dir = 2; cnt += 1
                            continue

                        # 종료 조건
                        if data[ty][tx] == -1 or (ty == i and tx == j): break

                        # 웜홀에 들어갔을 때
                        elif 6 <= data[ty][tx] <= 10:
                            halls = hall[data[ty][tx]]
                            if halls[0] == [ty, tx]:
                                ty, tx = halls[1][0], halls[1][1]
                                continue
                            else:
                                ty, tx = halls[0][0], halls[0][1]
                                continue

                        # 블록에 부딪혔을 때
                        elif 1 <= data[ty][tx] <= 5:
                            dir = change(dir, data[ty][tx])
                            cnt += 1

                    max_cnt = max(cnt, max_cnt)
    print('#{} {}'.format(tc + 1, max_cnt))

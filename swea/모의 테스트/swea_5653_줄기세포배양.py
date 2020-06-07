TC = int(input())
for tc in range(TC):
    R, C, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(R)]
    dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
    cells = {}
    for i in range(R):
        for j in range(C):
            if MAP[i][j] != 0:
                cells[(i, j)] = [0, MAP[i][j], MAP[i][j]]
    # print(cells)

    for _ in range(K):
        new_cell = {}
        for cell in cells:
            y, x = cell[0], cell[1]
            if cells[cell][0] == 2:
                continue
            elif cells[cell][0] == 0:
                cells[cell][1] -= 1
                if cells[cell][1] == 0:
                    cells[cell][0] = 1
                    cells[cell][1] = cells[cell][2]
            elif cells[cell][0] == 1:
                for dir in range(4):
                    ty, tx = y + dy[dir], x + dx[dir]
                    if (ty, tx) not in cells:
                        if (ty, tx) not in new_cell:
                            new_cell[(ty, tx)] = [0, cells[(y, x)][2], cells[(y, x)][2]]
                        else:
                            if new_cell[(ty, tx)][2] < cells[(y, x)][2]:
                                new_cell[(ty, tx)] = [0, cells[(y, x)][2], cells[(y, x)][2]]
                            else:
                                new_cell[(ty, tx)] = [0, new_cell[(ty, tx)][2], new_cell[(ty, tx)][2]]
                cells[cell][1] -= 1
                if cells[cell][1] == 0:
                    cells[cell][0] = 2

        cells.update(new_cell)
    answer = 0
    for cell in cells:
        if cells[cell][0] != 2:
            answer += 1
    print('#{} {}'.format(tc + 1, answer))



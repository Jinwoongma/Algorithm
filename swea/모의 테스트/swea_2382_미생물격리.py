def turn(d):
    if d == 1: return 2
    elif d == 2: return 1
    elif d == 3: return 4
    elif d == 4: return 3

TC = int(input())
for tc in range(TC):
    N, M, K = map(int, input().split())
    dy = [0, -1, 1, 0, 0]; dx = [0, 0, 0, -1, 1]
    cells = {}
    for i in range(K):
        y, x, k, d = map(int, input().split())
        cells[(y, x)] = [[k, d]]

    for _ in range(M):
        new_cells = {}
        del_cells = []
        for cell in cells:
            if not cells[cell]:
                continue
            y, x = cell
            k, d = cells[cell][0]
            ty, tx = y + dy[d], x + dx[d]
            if ty == 0 or ty == N - 1 or tx == 0 or tx == N - 1:
                k = k // 2
                d = turn(d)
                if k == 0:
                    cells[(y, x)].pop(0)
                    continue

            if (ty, tx) in cells:
                cells[(ty, tx)].append([k, d])
            else:
                if (ty, tx) in new_cells:
                    new_cells[(ty, tx)].append([k, d])
                else:
                    new_cells[(ty, tx)] = [[k, d]]
            cells[(y, x)].pop(0)

        cells.update(new_cells)

        for cell in cells:
            if len(cells[cell]) == 0:
                del_cells.append(cell)
            if len(cells[cell]) > 1:
                SUM, dir = 0, 0
                MAX = -1
                for c in cells[cell]:
                    SUM += c[0]
                    if c[0] > MAX:
                        MAX = c[0]
                        dir = c[1]
                cells[cell] = [[SUM, dir]]

        for cell in del_cells:
            cells.pop(cell)
        # print(cells)

    answer = 0
    for cell in cells:
        if cells[cell]:
            answer += cells[cell][0][0]

    print('#{} {}'.format(tc + 1, answer))
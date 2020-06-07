TC = int(input())
for tc in range(TC):
    N = int(input())
    dy = [0.5, -0.5, 0, 0]; dx = [0, 0, -0.5, 0.5]
    atoms = []
    for i in range(N):
        x, y, d, k = map(int, input().split())
        atoms.append([i, x, y, d, k])
    time = 1
    energy = 0
    while True:
        if time > 4000:
            break
        if len(atoms) < 2:
            break

        dic = {}
        for i in range(len(atoms)):
            index, x, y, d, k = atoms[i]
            atoms[i][1], atoms[i][2] = x + dx[d], y + dy[d]

        for i in atoms:
            index, x, y, d, k = i
            if (x, y) in dic:
                dic[(x, y)].append(i)
            else:
                dic[(x, y)] = [i]
        atoms = []

        for i in dic:
            if len(dic[i]) <= 1:
                item = dic[i]
                x = item[0][1]
                y = item[0][2]
                if x < -1000 or x > 1000 or y < -1000 or y > 1000:
                    pass
                else:
                    atoms.append(item[0])
            else:
                item = dic[i]
                for j in item:
                    energy += j[4]
        time += 1

    print('#{} {}'.format(tc + 1, energy))
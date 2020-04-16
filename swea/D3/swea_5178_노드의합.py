TC = int(input())
for tc in range(TC):
    N, M, L = map(int, input().split())
    MAX_node = -1
    data = []
    for i in range(M):
        node, val = map(int, input().split())
        data.append([node, val])
        MAX_node = max(MAX_node, node)

    values = [0 for _ in range(MAX_node + 1)]
    for node, val in data:
        values[node] = val

    for i in range(MAX_node, 0, -1):
        if values[i] == 0:
            if i * 2 + 1 > MAX_node:
                values[i] = values[i * 2]
            else:
                values[i] = values[i * 2] + values[i * 2 + 1]

        if i == L:
            print('#{} {}'.format(tc + 1, values[i]))
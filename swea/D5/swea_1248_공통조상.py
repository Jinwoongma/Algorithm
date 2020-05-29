from _collections import deque

def find_path(node, path):
    if node == 1:
        return path + [1]
    return find_path(U[node][0], path + [node])


def count_child(node):
    count = 1
    Q = deque()
    Q.append(node)
    while Q:
        p = Q.popleft()
        for c in D[p]:
            count += 1
            Q.append(c)
    return count


TC = int(input())
for tc in range(TC):
    V, E, a, b = map(int, input().split())
    U = [[] for _ in range(V + 1)]
    D = [[] for _ in range(V + 1)]
    nums = list(map(int, input().split()))
    for i in range(E):
        p, c = nums[i * 2], nums[i * 2 + 1]
        D[p].append(c)
        U[c].append(p)

    a_path = find_path(a, [])[::-1]
    b_path = find_path(b, [])[::-1]

    max_root = -1
    idx = 0
    while True:
        if idx >= len(a_path) or idx >= len(b_path):
            break
        if a_path[idx] == b_path[idx]:
            max_root = a_path[idx]
        idx += 1

    count = count_child(max_root)

    print('#{} {} {}'.format(tc + 1, max_root, count))


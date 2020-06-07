def search(tree, cur):
    global cnt
    if cur not in tree:
        return
    for w in tree[cur]:
        cnt += 1
        if w in tree:
            search(tree, w)

TC = int(input())
for tc in range(TC):
    T = dict()
    E, N = map(int, input().split())
    nums = list(map(int, input().split()))
    for i in range(E):
        p, c = nums[i * 2], nums[i * 2 + 1]
        if p in T.keys():
            T[p].append(c)
        else: T[p] = [c]

    cnt = 1
    search(T, N)
    print('#{} {}'.format(tc + 1, cnt))
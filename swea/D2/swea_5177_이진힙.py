TC = int(input())

for tc in range(TC):
    N = int(input())
    nums = list(map(int, input().split()))

    tree = [0]
    for num in nums:
        tree.append(num)
        now = len(tree) - 1
        while tree[now] < tree[now // 2]:
            tree[now], tree[now // 2] = tree[now // 2], tree[now]
            now //= 2

    result = 0
    node = len(tree) - 1
    while node // 2:
        result += tree[node // 2]
        node //= 2

    print('#{} {}'.format(tc + 1, result))
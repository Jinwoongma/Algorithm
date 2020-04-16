def makeTree(n, size):
    global cnt
    if n <= size:
        makeTree(n * 2, size)
        tree[n] = cnt  # 더이상 왼쪽에 자식이 없을 때
        cnt += 1
        makeTree(n * 2 + 1, size)  # 오른쪽 노드 탐색

TC = int(input())
for tc in range(TC):
    N = int(input())
    tree = [0] * (N + 1)
    cnt = 1
    makeTree(1, N)
    print('#{} {} {}'.format(tc + 1, tree[1], tree[N // 2]))

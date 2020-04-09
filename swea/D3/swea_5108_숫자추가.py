T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    lst = [i for i in map(int, input().split())]
    for _ in range(M):
        lst.insert(*map(int, input().split())) # 가변인자
    print('#{} {}'.format(test_case, lst[L]))
for tc in range(10):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        flag = 0
        for j in range(N):
            if magnetic[j][i] == 0: continue
            elif magnetic[j][i] == 1: flag = 1  # 붉은 자성체를 지나면 flag = 1
            elif flag == 1 and magnetic[j][i] == 2:  # 붉은 자성체를 지난 후에 푸른 자성체를 만남
                cnt += 1
                flag = 0
            elif flag == 0 and magnetic[j][i] == 2: continue
    print('#{} {}'.format(tc+1, cnt))
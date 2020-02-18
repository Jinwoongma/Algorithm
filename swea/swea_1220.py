import sys
sys.stdin = open("input_1220.txt", "r")

def transpose(arr):
    N = len(arr)
    new_arr = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[j][i]
    return new_arr

for tc in range(10):
    N = int(input())
    magnetic = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        flag = 0
        for j in range(N):
            if magnetic[j][i] == 0:
                continue
            elif magnetic[j][i] == 1:
                flag = 1
            elif flag == 1 and magnetic[j][i] == 2:
                cnt += 1
                flag = 0
            elif flag == 0 and magnetic[j][i] == 2:
                continue
    print('#{} {}'.format(tc+1, cnt))
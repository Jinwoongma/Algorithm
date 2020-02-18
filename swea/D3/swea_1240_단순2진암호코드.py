import sys
sys.stdin = open('input_1240.txt', 'r')

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    data = [str(input()) for _ in range(N)]
    code = ['0001101', '0011001', '0010011', '0111101', '0100011',
            '0110001', '0101111', '0111011', '0110111', '0001011']

    start_idx = 0
    flag = False
    for i in range(M-7):
        if flag: break
        for j in range(N):
            if flag: break
            temp = data[j][i:i+7]
            if temp != '0000000':
                num = []
                for k in range(len(code)):
                    if temp == code[k]:
                        for l in range(8):
                            temp = data[j][i + (l * 7) : i + (l * 7) + 7]
                            for m in range(len(code)):
                                if temp == code[m]:
                                    num.append(m)
                        if len(num) == 8:
                            flag = True
                            break

    if ((num[0] + num[2] + num[4] + num[6]) * 3 + num[1] + num[3] + num[5] + num[7]) % 10 == 0:
            print('#{} {}'.format(tc + 1, sum(num)))
    else:
        print('#{} {}'.format(tc + 1, 0))

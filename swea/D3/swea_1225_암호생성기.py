import sys
sys.stdin = open('input_1225.txt', 'r')

for tc in range(10):
    t = int(input())
    data = list(map(int, input().split()))
    sub = 1
    flag = True
    while flag:
        for sub in range(1, 6):
            temp = data[1:]
            if data[0] - sub <= 0:
                temp.append(0)
                data = temp
                flag = False
                break
            else:
                temp.append(data[0] - sub)
                data = temp

    print('#{} '.format(tc + 1), end='')
    print(" ".join(map(str, data)))



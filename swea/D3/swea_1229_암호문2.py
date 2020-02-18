import sys
sys.stdin = open('input_1230.txt', 'r')

for tc in range(10):
    L = int(input())
    data = list(map(str, input().split()))
    N = int(input())
    command = str(input()).replace('I', '.I').replace('D', '.D').split('.')[1:]
    # print(command)
    for i in range(len(command)):
        temp = command[i].split()
        # print(temp)
        if temp[0] == 'I':
            x, y, num = int(temp[1]), int(temp[2]), temp[3:]
            data = data[:x] + (num) + data[x:]

        elif temp[0] == 'D':
            x, y = int(temp[1]), int(temp[2])
            data = data[:x] + data[x+y:]

    print('#{} {}'.format(tc + 1, ' '.join(data[:10])))



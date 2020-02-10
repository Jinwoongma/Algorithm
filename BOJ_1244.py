N = int(input())
switch = list(map(int, input().split()))
s_num = int(input())
for s in range(s_num):
    sex, num = map(int, input().split())

    if sex == 1:
        for i in range(len(switch)):
            if (i+1) % num == 0:
                if switch[i] == 0: switch[i] = 1
                else: switch[i] = 0
            else:
                continue
    else:
        if num > len(switch)//2:
            max_len = len(switch) - num
        else:
            max_len = num - 1
        for i in range(max_len+1):
            if switch[num-1-i] == switch[num-1+i]:
                if switch[num-1-i] == 1: switch[num-1-i] = switch[num-1+i] = 0
                else: switch[num-1-i] = switch[num-1+i] = 1
            else:
                break

for i in range(len(switch)):
    if (i+1) % 20 == 0 and i != 0:
        print(switch[i])
    elif i == len(switch)-1:
        print(switch[i], end='')
    else:
        print(switch[i], end=' ')

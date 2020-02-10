import sys
sys.stdin = open('input_새로운 연산.txt', 'r')

base_num = [int(i * (i - 1) / 2) for i in range(1, 300)]

def num2cor(n):
    for num in range(300):
        if n > base_num[num] and n <= base_num[num + 1]:
            diff = base_num[num + 1] - n
            break
    return num + 1 - diff, 1 + diff

def cor2num(x, y):
    num = base_num[x + y - 1] - y + 1
    return num

TC = int(input())
for tc in range(TC):
    a, b = map(int, input().split())
    xa, ya = num2cor(a)
    xb, yb = num2cor(b)
    result = cor2num(xa + xb, ya + yb)
    print('#{} {}'.format(tc+1, result))
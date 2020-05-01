# 19:27 ~ 19:47
from _collections import deque
from copy import deepcopy

wheel = []
for i in range(4):
    wheel.append(deque(list(map(int, input().strip()))))
N = int(input())

for i in range(N):
    index, dir = map(int, input().split())
    index -= 1
    temp = deepcopy(wheel)
    temp[index].rotate(dir)

    j, d = index, dir
    while True:
        if j == 3: break
        if wheel[j][2] != wheel[j + 1][6]:
            d *= -1
            temp[j + 1].rotate(d)
            j += 1
        else: break

    j, d = index, dir
    while True:
        if j == 0: break
        if wheel[j][6] != wheel[j - 1][2]:
            d *= -1
            temp[j - 1].rotate(d)
            j -= 1
        else: break
    wheel = temp

score = 0
if wheel[0][0]: score += 1
if wheel[1][0]: score += 2
if wheel[2][0]: score += 4
if wheel[3][0]: score += 8
print(score)
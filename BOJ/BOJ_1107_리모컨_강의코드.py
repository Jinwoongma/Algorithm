# 이동하는 채널(C)을 정한다.
# C에 고장난 버튼이 있는지 확인한다.
# 고장난 버튼이 포함되어있지 않다면, abs(C-N)을 계산하여 +나 -를 몇번 눌러야하는지 계산한다.

goal = int(input())
trouble_num = int(input())
min_push = abs(goal - 100)

if trouble_num != 0:
    trouble = list(map(int, input().split()))
else: trouble = []

for num in range(1000000):
    for char_num in str(num):
        if int(char_num) in trouble:
            break
    else:
        push = len(str(num)) + abs(goal - num)
        min_push = min(min_push, push)

print(min_push)
def turn(n, dir):
    if dir == 1:
        wheel[n][0], wheel[n][1:] = wheel[n][-1], wheel[n][:-1]
    elif dir == -1:
        wheel[n][:-1], wheel[n][-1] = wheel[n][1:], wheel[n][0]

wheel = [list(map(int, input().strip())) for _ in range(4)]
N = int(input())

for i in range(N):
    num, dir = map(int, input().split())
    num -= 1
    temp = [[0 for _ in range(8)] for _ in range(4)]
    turn_lst = [[num, dir]]
    new_dir = dir
    if num != 3:
        flag = True
        for j in range(num, 3):
            new_dir *= -1
            if wheel[j][2] != wheel[j + 1][6] and flag:
                turn_lst.append([j + 1, new_dir])
            else:
                flag = False

    new_dir = dir
    if num != 0:
        flag = True
        for j in range(num, 0, -1):
            new_dir *= -1
            if wheel[j][6] != wheel[j - 1][2] and flag:
                turn_lst.append([j - 1, new_dir])
            else:
                flag = False

    for n, d in turn_lst:
        turn(n, d)

score = wheel[0][0] * 1 + wheel[1][0] * 2 + wheel[2][0] * 4 + wheel[3][0] * 8
print(score)
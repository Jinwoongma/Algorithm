omok = [list(map(int, input().split())) for _ in range(19)]
dx = [1, 0, 1, 1]  # 오른, 아래, 오른대각아래, 오른대각위
dy = [0, 1, 1, -1]
flag = False
ans_x, ans_y, ans_num = -1, -1, -1

def is_range(y, x):
    if x < 0 or y < 0 or x >= 19 or y >= 19:
        return False
    else:
        return omok[y][x]

for dir in range(4):
    for j in range(19):
        for k in range(19):
            if omok[j][k] == 0:
                continue

            if omok[j][k] == is_range(j-dy[dir], k-dx[dir]):
                continue

            new_y, new_x, cnt = j, k, 0
            while True:
                new_x += dx[dir]
                new_y += dy[dir]
                if not is_range(new_y, new_x):
                    break
                if omok[j][k] != omok[new_y][new_x]:
                    break
                cnt += 1

            if cnt == 4:
                flag = True
                ans_y = j + 1
                ans_x = k + 1
                ans_num = omok[j][k]
                break

if flag == True:
    print(ans_num)
    print(ans_y, ans_x)
else:
    print(0)



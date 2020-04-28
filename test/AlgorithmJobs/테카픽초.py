def fill():
    for r in range(R):
        flag = False
        temp = []
        for c in range(C):
            if check[r][c] == 1:
                if flag: flag = False
                else: flag = True
            else:
                if flag: temp.append([r, c])
        if not flag:
            for y, x in temp:
                check[y][x] = 1

def isAllEven():
    for r in range(R):
        for c in range(C):
            if check[r][c] == 1:
                if MAP[r][c] % 2 == 1:
                    return False
    return True

R, C = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(R)]
answer = 0

L = min(R, C)
for i in range(R - 2):
    for j in range(1, C - 1):
        for d1 in range(1, L):
            for d2 in range(1, L):
                if i + d1 + d2 < R and 0 <= j - d1 and j + d2 < C:
                    check = [[0 for _ in range(C)] for _ in range(R)]
                    y, x = i, j
                    for k in range(d1 + 1):
                        check[y][x] = 1
                        y += 1; x -= 1


                    y, x = i, j
                    for k in range(d2 + 1):
                        check[y][x] = 1
                        y += 1; x += 1

                    y, x = i + d1, j - d1
                    for k in range(d2 + 1):
                        check[y][x] = 1
                        y += 1; x += 1

                    y, x = i + d2, j + d2
                    for k in range(d1 + 1):
                        check[y][x] = 1
                        y += 1; x -= 1

                    fill()
                    if isAllEven():
                        answer += 1
print(answer)


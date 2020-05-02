# 20/05/02 16:55 ~ 17:48

def transpose(arr, R, C):
    new_arr = [[0 for _ in range(R)] for _ in range(C)]
    for i in range(R):
        for j in range(C):
            new_arr[j][i] = arr[i][j]
    return new_arr


r, c, k = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(3)]
time = 0
answer = -1
while True:
    # 종료 조건
    if time > 100: break
    if len(MAP) >= r and len(MAP[0]) >= c:
        if MAP[r - 1][c - 1] == k:
            answer = time
            break

    # 연산
    if len(MAP) >= len(MAP[0]):  # 행 >= 열, R 연산
        new_MAP = []
        length = 0
        for i in range(len(MAP)):
            temp = {}
            for j in range(len(MAP[0])):
                if MAP[i][j] == 0: continue
                if MAP[i][j] in temp: temp[MAP[i][j]] += 1
                else: temp[MAP[i][j]] = 1
            stemp = sorted(temp.items(), key=lambda x: (x[1], x[0]))
            S = []
            for index, cnt in stemp:
                S.append(index)
                S.append(cnt)
            length = max(length, len(S))
            new_MAP.append(S)

        # 0 채우기
        for i in range(len(MAP)):
            new_MAP[i] += [0] * (length - len(new_MAP[i]))
            if len(new_MAP[i]) > 100:
                new_MAP[i] = new_MAP[i][:100]
        MAP = new_MAP

    else:  # 행 < 열, C 연산
        new_MAP = []
        length = 0
        for i in range(len(MAP[0])):
            temp = {}
            for j in range(len(MAP)):
                if MAP[j][i] == 0: continue
                if MAP[j][i] in temp:
                    temp[MAP[j][i]] += 1
                else:
                    temp[MAP[j][i]] = 1
            stemp = sorted(temp.items(), key=lambda x: (x[1], x[0]))
            S = []
            for index, cnt in stemp:
                S.append(index)
                S.append(cnt)
            length = max(length, len(S))
            new_MAP.append(S)

        # 0 채우기
        for i in range(len(new_MAP)):
            new_MAP[i] += [0] * (length - len(new_MAP[i]))
            if len(new_MAP[i]) > 100:
                new_MAP[i] = new_MAP[i][:100]
        MAP = transpose(new_MAP, len(new_MAP), len(new_MAP[0]))

    time += 1

print(-1 if answer == -1 else answer)

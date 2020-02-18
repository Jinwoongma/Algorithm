# 파일명 및 함수명을 변경하지 마시오.
# 추가 모듈이나 패키지를 import 할 수 없습니다.
import copy
N = int(input())
data = []
ans = 0
for i in range(N):
    temp = list(map(int, input().split()))
    data.append(temp)

def move(dir):
    if dir == 1:  # 오른쪽 이동
        for i in range(N):
            for j in range(N - 1, 0, -1):
                if data[i][j] == 0:
                    continue
                else:
                    for k in range(j - 1, -1, -1):
                        if data[i][k] == 0:
                            continue
                        elif data[i][j] != data[i][k]:
                            break
                        elif data[i][j] == data[i][k]:
                            data[i][j] *= 2
                            data[i][k] = 0
                            break

            for j in range(N - 1, 0, -1):
                if data[i][j] != 0:
                    continue
                else:
                    for k in range(j - 1, -1, -1):
                        if data[i][k] != 0:
                            data[i][j], data[i][k] = data[i][k], data[i][j]
                            break

    elif dir == 2:  # 왼쪽 이동
        for i in range(N):
            for j in range(0, N - 1):
                if data[i][j] == 0:
                    continue
                else:
                    for k in range(j + 1, N):
                        if data[i][k] == 0:
                            continue
                        elif data[i][j] != data[i][k]:
                            break
                        elif data[i][j] == data[i][k]:
                            data[i][j] *= 2
                            data[i][k] = 0
                            break

            for j in range(0, N - 1):
                if data[i][j] != 0:
                    continue
                else:
                    for k in range(j + 1, N):
                        if data[i][k] != 0:
                            data[i][j], data[i][k] = data[i][k], data[i][j]
                            break


    elif dir == 3:  # 위로 이동
        for i in range(N):
            for j in range(0, N - 1):
                if data[j][i] == 0:
                    continue
                else:
                    for k in range(j + 1, N):
                        if data[k][i] == 0:
                            continue
                        elif data[j][i] != data[k][i]:
                            break
                        elif data[j][i] == data[k][i]:
                            data[j][i] *= 2
                            data[k][i] = 0
                            break

            for j in range(0, N - 1):
                if data[j][i] != 0:
                    continue
                else:
                    for k in range(j + 1, N):
                        if data[k][i] != 0:
                            data[j][i], data[k][i] = data[k][i], data[j][i]
                            break

    elif dir == 4:  # 아래로 이동
        for i in range(N):
            for j in range(N - 1, 0, -1):
                if data[j][i] == 0:
                    continue
                else:
                    for k in range(j - 1, -1, -1):
                        if data[k][i] == 0:
                            continue
                        elif data[j][i] != data[k][i]:
                            break
                        elif data[j][i] == data[k][i]:
                            data[j][i] *= 2
                            data[k][i] = 0
                            break

            for j in range(N - 1, 0, -1):
                if data[j][i] != 0:
                    continue
                else:
                    for k in range(j - 1, -1, -1):
                        if data[k][i] != 0:
                            data[j][i], data[k][i] = data[k][i], data[j][i]
                            break
    return data

def solve(cnt):
    global ans, data
    if cnt == 5:
        for i in range(N):
            if ans <= max(data[i]):
                #print(data[i])
                ans = max(data[i])
        return
    b = copy.deepcopy(data)

    for k in range(1, 5):
        move(k)
        solve(cnt + 1)
        data = copy.deepcopy(b)

solve(0)
print(ans)
N, L = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(N)]
count = 0

def search(next, y, x, ud, gs):
    if ud == 'D':
        for i in range(1, L + 1):
            if gs == 'g':
                tx = x + i
                if tx >= N: return False
                if next != MAP[y][tx] or check[y][tx]: return False
                check[y][tx] = True
            elif gs == 's':
                ty = y + i
                if ty >= N: return False
                if next != MAP[ty][x] or check[ty][x]: return False
                check[ty][x] = True
        return True

    elif ud == 'U':
        for i in range(0, L):
            if gs == 'g':
                tx = x - i
                if tx < 0: return False
                if next != MAP[y][tx] or check[y][tx]: return False
                check[y][tx] = True
            elif gs == 's':
                ty = y - i
                if ty < 0: return False
                if next != MAP[ty][x] or check[ty][x]: return False
                check[ty][x] = True
        return True


# 가로 길 체크
check = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N - 1):
        if abs(MAP[i][j] - MAP[i][j + 1]) == 0:
            continue
        if abs(MAP[i][j] - MAP[i][j + 1]) >= 2:
            break

        if MAP[i][j] > MAP[i][j + 1]:  # 현재 높이가 더 높은 경우 (아래로 경사로 설치)
            if not search(MAP[i][j + 1], i, j, 'D', 'g'):
                break
        elif MAP[i][j] < MAP[i][j + 1]:
            if not search(MAP[i][j], i, j, 'U', 'g'):
                break
        else: continue
    else:
        count += 1  # 끝까지 왔으면 가능한 경로 + 1

# 세로 길 체크
check = [[False for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N - 1):
        if abs(MAP[j][i] - MAP[j + 1][i]) == 0:
            continue
        if abs(MAP[j][i] - MAP[j + 1][i]) >= 2:
            break

        if MAP[j][i] > MAP[j + 1][i]:  # 현재 높이가 더 높은 경우 (아래로 경사로 설치)
            if not search(MAP[j + 1][i], j, i, 'D', 's'):
                break
        elif MAP[j][i] < MAP[j + 1][i]:
            if not search(MAP[j][i], j, i, 'U', 's'):
                break
        else: continue
    else:
        count += 1  # 끝까지 왔으면 가능한 경로 + 1

print(count)
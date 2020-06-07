cctv1 = [[[-1, 0]],
         [[0, 1]],
         [[1, 0]],
         [[0, -1]]]

cctv2 = [[[0, -1], [0, 1]],
         [[-1, 0], [1, 0]]]

cctv3 = [[[-1, 0], [0, 1]],
         [[0, 1], [1, 0]],
         [[1, 0], [0, -1]],
         [[0, -1], [-1, 0]]]

cctv4 = [[[0, -1], [-1, 0], [0, 1]],
         [[-1, 0], [0, 1], [1, 0]],
         [[0, 1], [1, 0], [0, -1]],
         [[1, 0], [0, -1], [-1, 0]]]

cctv5 = [[[1, 0], [-1, 0], [0, 1], [0, -1]]]

def search(cctv, y, x):
    count = 0
    for k in range(len(cctv)):
        ty, tx = y, x
        while True:
            ty += cctv[k][0]
            tx += cctv[k][1]
            if ty < 0 or ty >= r or tx < 0 or tx >= c: break
            if MAP[ty][tx] == 6: break
            if 1 <= MAP[ty][tx] <= 5: continue
            if MAP[ty][tx] == 0:
                check[ty][tx] += 1
                if check[ty][tx] == 1:
                    count += 1
    return count


def erase(cctv, y, x):
    count = 0
    for k in range(len(cctv)):
        ty, tx = y, x
        while True:
            ty += cctv[k][0]
            tx += cctv[k][1]
            if ty < 0 or ty >= r or tx < 0 or tx >= c: break
            if MAP[ty][tx] == 6: break
            if 1 <= MAP[ty][tx] <= 5: continue
            if MAP[ty][tx] == 0:
                check[ty][tx] -= 1
                if check[ty][tx] == 0:
                    count += 1
    return count


def dfs(index, count, start):
    global min_safe
    if index == N:
        safe = (r * c) - no_count - count
        min_safe = min(min_safe, safe)
        return

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            y, x, n = cctv[i]
            if n == 1:
                for j in range(4):
                    count += search(cctv1[j], y, x)
                    dfs(index + 1, count, i)
                    count -= erase(cctv1[j], y, x)

            elif n == 2:
                for j in range(2):
                    count += search(cctv2[j], y, x)
                    dfs(index + 1, count, i)
                    count -= erase(cctv2[j], y, x)

            elif n == 3:
                for j in range(4):
                    count += search(cctv3[j], y, x)
                    dfs(index + 1, count, i)
                    count -= erase(cctv3[j], y, x)
            elif n == 4:
                for j in range(4):
                    count += search(cctv4[j], y, x)
                    dfs(index + 1, count, i)
                    count -= erase(cctv4[j], y, x)

            elif n == 5:
                for j in range(1):
                    count += search(cctv5[j], y, x)
                    dfs(index + 1, count, i)
                    count -= erase(cctv5[j], y, x)

            visited[i] = False


r, c = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(r)]
no_count = 0
cctv = []
for i in range(r):
    for j in range(c):
        if 1 <= MAP[i][j] <= 5:
            cctv.append([i, j, MAP[i][j]])
            no_count += 1
        elif MAP[i][j] == 6:
            no_count += 1
N = len(cctv)
visited = [False for _ in range(N)]
check = [[0 for _ in range(c)] for _ in range(r)]
min_safe = 0xffffffff
dfs(0, 0, 0)
print(min_safe)

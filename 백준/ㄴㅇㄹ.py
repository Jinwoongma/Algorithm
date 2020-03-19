def is_covered(a, b, s):
    for i in range(a, a + s):
        for j in range(b, b + s):
            if not board[i][j]:
                return False
    return True


def toggle_visited(a, b, s):
    for i in range(a, a + s):
        for j in range(b, b + s):
            if visited[i][j]:
                visited[i][j] = 0
            else:
                visited[i][j] = 1


def get_used_cnt(c):
    global result
    if visited == board:
        result = c
        return
    if c > result:
        return
    for i in range(10):
        for j in range(10):
            if board[i][j] and not visited[i][j]:
                for size in range(5, 0, -1):
                    if i + size >= 10 or j + size >= 10: continue
                    if not is_covered(i, j, size): continue
                    if colors[size] - 1 < 0: continue
                    if colors[1] - 1 < 0: return
                    colors[size] -= 1
                    toggle_visited(i, j, size)
                    get_used_cnt(c + 1)
                    colors[size] += 1
                    toggle_visited(i, j, size)


board = [list(map(int, input().split())) for _ in range(10)]
colors = [0, 5, 5, 5, 5, 5]
visited = [[0] * 10 for _ in range(10)]
result = 25
get_used_cnt(0)
if result == 25:
    result = -1
print(result)
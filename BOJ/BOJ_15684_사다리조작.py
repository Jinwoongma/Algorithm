def selectLine(index, cnt):
    global ans
    if cnt >= 4:
        return
    if ladderGame():
        ans = min(ans, cnt)
        return

    for i in range(index, h + 1):
        for j in range(1, s):
            if visited[j][i]: continue
            if visited[j - 1][i]: continue
            if visited[j + 1][i]: continue

            visited[j][i] = 1
            selectLine(i, cnt + 1)
            visited[j][i] = 0


def ladderGame():
    for i in range(1, s + 1):
        index, height = i, 1
        while True:
            if height == h + 1: break
            if visited[index][height]:
                index += 1
                height += 1
                continue
            elif visited[index - 1][height]:
                index -= 1
                height += 1
                continue
            else:
                height += 1
        if index == i:
            continue
        else:
            return False
    return True


s, g, h = map(int, input().split())
visited = [[0 for _ in range(h + 1)] for _ in range(s + 1)]
ans = 0xffffffff
for i in range(g):
    height, index = map(int, input().split())
    visited[index][height] = 1

selectLine(1, 0)
if ans == 0xffffffff:
    print (-1)
else:
    print(ans)
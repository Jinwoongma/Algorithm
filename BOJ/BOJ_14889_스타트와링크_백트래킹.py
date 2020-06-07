def solve(index, first, second):
    if index == N:
        if len(first) != N // 2: return -1
        if len(second) != N // 2: return -1
        t1, t2 = 0, 0
        for i in range(N//2):
            for j in range(N//2):
                if i == j: continue
                t1 += data[first[i]][first[j]]
                t2 += data[second[i]][second[j]]
        diff = abs(t1 - t2)
        return diff

    if len(first) > N // 2: return -1
    if len(second) > N // 2: return -1

    ans = -1
    first.append(index)
    t1 = solve(index + 1, first, second)
    if ans == -1 or (t1 != -1 and t1 < ans):
        ans = t1
    first.pop()

    second.append(index)
    t2 = solve(index + 1, first, second)
    if ans == -1 or (t2 != -1 and t2 < ans):
        ans = t2
    second.pop()

    return ans


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
result, arr = [], []
min_diff = 0xffffffff
start, link = [], []
print(solve(0, start, link))
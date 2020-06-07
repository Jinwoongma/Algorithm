def solve(index):
    global cnt
    if cnt == N:
        print(' '.join(map(str, data)))
        return
    if index == 10:
        return
    for i in range(1, 5):
        if i != 1:
            cnt += 1
        data[index] = i
        solve(index + 1)
        data[index] = 1



N = int(input())
data = [1] * 10
cnt = 1
solve(0)
def dfs(index):
    global count
    if index == N:
        count += 1
        return
    for i in range(N):
        row[index] = i
        if isprommsing(index):
            dfs(index + 1)


def isprommsing(index):
    for i in range(index):
        if row[i] == row[index] or abs(row[i] - row[index]) == index - i:
            return False
    return True


N = int(input())
row = [0] * N
count = 0
dfs(0)
print(count)
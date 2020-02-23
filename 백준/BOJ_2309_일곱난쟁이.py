def combi(index):
    global flag
    if index == 7:
        if sum(arr) == 100:
            flag = True
            return
        else: return

    for i in range(9):
        if not visited[i]:
            visited[i] = True
            arr.append(height[i])
            combi(index + 1)
            if flag: return
            visited[i] = False
            arr.pop()

height = []
for i in range(9):
    height.append(int(input()))
visited = [False for _ in range(9)]
flag = False
arr = []
combi(0)
arr.sort()
for i in range(7):
    print(arr[i])
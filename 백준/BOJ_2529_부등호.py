def combi(index):
    global max_value
    global min_value
    global result

    if index == N + 1:
        for i in range(N):
            if assign[i] == '>':
                if arr[i] < arr[i + 1]: break
            elif assign[i] == '<':
                if arr[i] > arr[i + 1]: break
        else:
            temp = int(''.join(map(str, arr)))
            temp2 = arr[:]
            if temp > max_value:
                max_value = temp
                result[0] = temp2
            if temp < min_value:
                min_value = temp
                result[1] = temp2
        return
    for i in range(10):
        if not visited[i]:
            visited[i] = True
            arr.append(i)
            combi(index + 1)
            visited[i] = False
            arr.pop()


N = int(input())
visited = [False for _ in range(10)]
assign = list(map(str, input().split()))
min_value, max_value = 10000000000, -1
result = [[],[]]
arr = []
combi(0)
print(''.join(map(str, result[0])))
print(''.join(map(str, result[1])))

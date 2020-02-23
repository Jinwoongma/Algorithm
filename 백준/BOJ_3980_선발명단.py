def solution(index):
    global max_value
    if index == 12:
        max_value = max(max_value, sum(arr))
        return
    for p in position[index]:
        if not visited[p]:
            arr.append(data[index - 1][p - 1])
            visited[p] = True
            solution(index + 1)
            visited[p] = False
            arr.pop()

TC = int(input())
for tc in range(TC):
    data = [list(map(int, input().split())) for _ in range(11)]
    position = [[] for _ in range(12)]
    visited = [False for _ in range(12)]

    for i in range(11):
        for j in range(11):
            if data[i][j] != 0:
                position[i + 1].append(j + 1)

    max_value = -1
    arr = []
    solution(1)
    print(max_value)
N = int(input())
data = list(map(int, input().split()))
max_diff = -1
path = []
up = False
temp = -1

for i in range(N):
    if data[i] > temp:
        up = True
        path.append(data[i])
    else:
        up = False
        path = []
        path.append(data[i])
    temp = data[i]

    if up:
        diff = path[-1] - path[0]
        if diff >= max_diff:
            max_diff = diff

print(max_diff)
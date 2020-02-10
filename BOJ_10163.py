N = int(input())
color_map = [[0 for _ in range(101)] for _ in range(101)]
for i in range(1, N+1):
    x, y, w, h = map(int, input().split())
    for col in range(y, y + h):
        for row in range(x, x + w):
            if color_map[col][row] == 0:
                color_map[col][row] = i
            elif i > color_map[col][row]:
                color_map[col][row] = i
            else:
                continue

# for i in range(10):
#     print(color_map[i])
# print()

for i in range(1, N+1):
    count = 0
    for j in range(101):
        for k in range(101):
            if color_map[j][k] == i:
                count += 1
    print(count)
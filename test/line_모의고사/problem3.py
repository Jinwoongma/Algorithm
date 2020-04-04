N = int(input())
table = []
for i in range(N):
  IN, OUT = map(int, input().split())
  table.append((IN, OUT))
table.sort(key=lambda x: x[0])
print(table)

times = []
for IN, OUT in table:
    flag = False
    for i in range(len(times)):
        if times[i] <= IN:
            times[i] = OUT
            flag = True
    if not flag:
        times.append(OUT)

print(len(times))

############################################

# N = int(input())
# start, end = 0, 0
# check = [0] * 160
# MAX = 0
#
# for i in range(N):
#     IN, OUT = map(int, input().split())
#     for j in range(IN, OUT):
#         check[j] += 1
#         if MAX < check[j]:
#             MAX = check[j]
#
# print(MAX)
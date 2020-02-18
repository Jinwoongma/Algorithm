M, N = map(int, input().split())
K = int(input())
garo_lst, sero_lst = [], []

for i in range(K):
    dir, num = map(int, input().split())
    if dir == 0:
        if 0 < num <= N:
            garo_lst.append(num)
    else:
        if 0 < num <= M:
            sero_lst.append(num)

garo_lst.append(N)
sero_lst.append(M)

garo_lst.sort()
sero_lst.sort()
# print(garo_lst, sero_lst)

garo_length, sero_length = [], []
for i in range(len(garo_lst)):
    if i == 0:
        garo_length.append(garo_lst[i])
    else:
        garo_length.append(garo_lst[i] - garo_lst[i - 1])

for i in range(len(sero_lst)):
    if i == 0:
        sero_length.append(sero_lst[i])
    else:
        sero_length.append(sero_lst[i] - sero_lst[i - 1])

# print(garo_length, sero_length)
garo_length.sort()
sero_length.sort()

print(garo_length[-1] * sero_length[-1])

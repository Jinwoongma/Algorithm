N = int(input())
data = []
temp = {}
for i in range(N):
    data = list(map(str, input().strip()))
    for j in range(len(data)):
        if data[j] in temp.keys():
            temp[data[j]] += 10 **(len(data) - j - 1)
        else:
            temp[data[j]] = 10 ** (len(data) - j - 1)

temp2 = []
for key, value in temp.items():
    temp2.append([key, value])
temp2 = sorted(temp2, key = lambda x: x[1], reverse=True)

result = 0
for i in range(len(temp2)):
    result += (temp2[i][1] * (9 - i))
print(result)


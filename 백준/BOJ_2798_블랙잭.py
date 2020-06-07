def combi(k, s):
    global sum_
    if k == 3:
        sum_ = sum(result)
        sums.append(sum_)
    else:
        for i in range(s, N):
            result[k] = cards[i]
            combi(k + 1, i + 1)

N, M = map(int, input().split())
cards = list(map(int, input().split()))
result = [0] * 3
sums = []
max_sum = -1
combi(0, 0)

for sum in sums:
    if sum > M:
        continue
    else:
        if sum >= max_sum:
            max_sum = sum
print(max_sum)
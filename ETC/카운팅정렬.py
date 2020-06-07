arr = [69, 10, 30, 2, 16, 8, 31, 22]
K = max(arr)
result = [0] * len(arr)
cnt = [0] * (K + 1)

for val in arr:
    cnt[val] += 1

for i in range(1, K + 1):
    cnt[i] += cnt[i - 1]

for i in range(len(arr) - 1, -1, -1):
    cnt[arr[i]] -= 1
    result[cnt[arr[i]]] = arr[i]

print(result)
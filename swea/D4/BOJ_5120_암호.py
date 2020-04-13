TC = int(input())

for a in range(TC):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))
    now = 0
    for _ in range(K):
        position = (now + M) % len(arr)
        value = arr[position - 1] + arr[position]
        if position == 0:
            arr.append(value)
            now = -1
        else:
            arr.insert(position, value)
            now = position
    if len(arr) <= 10:
        print('#{} {}'.format(tc + 1, ' '.join([str(num) for num in arr[::-1]])))
    elif len(arr) > 10:
        result = []
        count = 0
        for num in arr[::-1]:
            count += 1
            result.append(str(num))
            if count == 10:
                break
        print('#{} {}'.format(tc + 1, ' '.join(result)))
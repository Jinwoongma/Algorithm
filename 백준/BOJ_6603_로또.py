def combi(index):
    if index == 6:
        print(' '.join(map(str, arr)))
        return

    for i in range(k):
        if not visited[i]:
            if len(arr) == 0:
                arr.append(s[i])
            else:
                if s[i] > arr[-1]:
                    arr.append(s[i])
                else: continue
            visited[i] = True
            combi(index + 1)
            visited[i] = False
            arr.pop()

while True:
    num = list(map(int, input().split()))
    if len(num) == 1 and num[0] == 0:
        break
    k, s = num[0], num[1:]
    visited = [False for _ in range(k)]
    arr = []
    combi(0)
    print()

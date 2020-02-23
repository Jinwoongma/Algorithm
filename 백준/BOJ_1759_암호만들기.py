def combi(index):
    if index == r:
        mo_cnt, ja_cnt = 0, 0
        for i in range(r):
            if arr[i] in 'aeiou':
                mo_cnt += 1
            else: ja_cnt += 1
        if mo_cnt >= 1 and ja_cnt >= 2:
            print(''.join(map(str, arr)))
        return

    for i in range(n):
        if not visited[i]:
            if len(arr) == 0:
                arr.append(char[i])
            else:
                if ord(char[i]) > ord(arr[-1]):
                    arr.append(char[i])
                else: continue
            visited[i] = True
            combi(index + 1)
            visited[i] = False
            arr.pop()



r, n = map(int, input().split())
char = list(map(str, input().split()))
char.sort()
visited = [False for _ in range(n)]
arr = []
combi(0)
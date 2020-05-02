from _collections import deque

subin, sister = map(int, input().split())
visited = [0 for _ in range(100001)]
visited[subin] = True
Q = deque()
Q.append([subin, 0])
answer = -1
while Q:
    subin, time = Q.popleft()
    if subin == sister:
        answer = time
        break
    nsubin = (subin - 1, subin + 1, subin * 2)
    for n in nsubin:
        if n < 0 or n > 100000: continue
        if not visited[n]:
            visited[n] = True
            Q.append([n, time + 1])
print(answer)
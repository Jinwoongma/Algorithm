from _collections import deque

def check_s(arr):
    s_count = 0
    for i in range(7):
        if MAP[(arr[i] - 1) // 5][(arr[i] - 1) % 5] == 'S':
            s_count += 1
    if s_count >= 4: return True
    else: return False


def check_adj(arr):
    Q = deque()
    Q.append(arr[0])
    visited2 = [False for _ in range(26)]
    visited2[arr[0]] = True
    count = 0
    while Q:
        s = Q.popleft()
        for w in G[s]:
            if not visited2[w] and w in arr:
                visited2[w] = True
                count += 1
                Q.append(w)
    return count


def combi(index, s):
    global count
    global result
    if index == 7:
        if check_s(arr):
            if check_adj(arr) == 6:
                result += 1
        return
    for i in range(s, 25):
        if not visited[i]:
            arr.append(i + 1)
            visited[i] = True
            combi(index + 1, i + 1)
            visited[i] = False
            arr.pop()


MAP = [list(map(str, input().strip())) for _ in range(5)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
visited = [False for _ in range(25)]
G = [[] for _ in range(26)]

for i in range(1, 26):
    if (i - 1) // 5 == 0:
        if (i - 1) % 5 == 0:
            G[i].append(i + 1)
            G[i].append(i + 5)
        elif (i - 1) % 5 == 4:
            G[i].append(i - 1)
            G[i].append(i + 5)
        else:
            G[i].append(i - 1)
            G[i].append(i + 1)
            G[i].append(i + 5)

    elif (i - 1) // 5 == 4:
        if (i - 1) % 5 == 0:
            G[i].append(i + 1)
            G[i].append(i - 5)
        elif (i - 1) % 5 == 4:
            G[i].append(i - 1)
            G[i].append(i - 5)
        else:
            G[i].append(i - 1)
            G[i].append(i + 1)
            G[i].append(i - 5)
    else:
        if (i - 1) % 5 == 0:
            G[i].append(i + 1)
            G[i].append(i - 5)
            G[i].append(i + 5)
        elif (i - 1) % 5 == 4:
            G[i].append(i - 1)
            G[i].append(i - 5)
            G[i].append(i + 5)
        else:
            G[i].append(i + 1)
            G[i].append(i - 1)
            G[i].append(i + 5)
            G[i].append(i - 5)

arr = []
result = 0
combi(0, 0)
print(result)
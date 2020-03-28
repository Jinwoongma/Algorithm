answer = 0
result = []


def dfs(index, G, visited, N, path):
    global answer
    global result
    if index == N:
        path = sorted(path)
        if path not in result:
            result.append(path[:])
            answer += 1
    else:
        for w in G[index]:
            if not visited[w]:
                visited[w] = True
                path.append(w)
                dfs(index + 1, G, visited, N, path)
                visited[w] = False
                path.pop()



def solution(user_id, banned_id):
    dic = {}
    for i in range(len(user_id)):
        dic[user_id[i]] = i

    G = [[] for _ in range(len(user_id))]
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if len(banned_id[i]) == len(user_id[j]):
                for k in range(len(banned_id[i])):
                    if banned_id[i][k] != '*' and banned_id[i][k] != user_id[j][k]:
                        break
                else:
                    G[i].append(j)
    print(G)
    visited = [False] * (len(user_id))
    dfs(0, G, visited, len(banned_id), [])
    return answer


user_id = ["frodo", '4']
banned_id = ["*", '*rodo']
print(solution(user_id, banned_id))

from _collections import deque
answer = 0

def cal(sign, arr):
    for s in sign:
        arr = deque(arr)
        new_arr = []
        while arr:
            a = arr.popleft()
            if a != s:
                new_arr.append(a)
            else:
                n1 = new_arr.pop()
                sign = a
                n2 = arr.popleft()
                if sign == '*':
                    temp = int(n1) * int(n2)
                elif s == '+':
                    temp = int(n1) + int(n2)
                elif s == '-':
                    temp = int(n1) - int(n2)
                new_arr.append(temp)
        arr = new_arr
    return abs(arr[0])


def permutation(index, signs, arr, visited, S):
    global answer
    if index == len(signs):
        ret = cal(arr, S)
        answer = max(answer, ret)
        return
    for i in range(len(signs)):
        if not visited[i]:
            visited[i] = True
            arr.append(signs[i])
            permutation(index + 1, signs, arr, visited, S)
            arr.pop()
            visited[i] = False


def solution(expression):
    signs = set()
    S = []
    temp = ''
    for c in expression:
        if c not in '+-*':
            temp += c
        else:
            signs.add(c)
            S.append(temp)
            temp = ''
            S.append(c)
    S.append(temp)

    visited = [False for _ in range(len(signs))]
    permutation(0, list(signs), [], visited, S)
    return answer

print(solution("100-200*300-500+20"))
def isComplete(s):
    S = []
    for i in range(len(s)):
        if len(S) == 0:
            S.append(s[i])
        else:
            if s[i] == '(':
                S.append(s[i])
            else:
                if S.pop() == '(': continue
                else: return False
    if len(S) > 0: return False
    return True


def truncate(s):
    ret1, ret2 = '', ''
    open, close = 0, 0
    start = 0
    for i in range(len(s)):
        ret1 += s[i]
        if s[i] == '(': open += 1
        else: close += 1
        if open == close:
            start = i + 1
            break
    ret2 = s[start:]
    return ret1, ret2


def solution(p):
    if p == '':
        return p
    u, v = truncate(p)
    if isComplete(u):
        return u + solution(v)
    else:
        temp = ''
        for i in range(1, len(u) - 1):
            if u[i] == '(': temp += ')'
            else: temp += '('
        return '(' + solution(v) + ')' + temp


INPUT = [
    '(()())()',
    ')(',
    '()))((()'
]
for a in INPUT:
    print(solution(a))
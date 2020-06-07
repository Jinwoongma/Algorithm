def solution(inputString):
    S = []
    cnt = 0
    flag = True

    for char in inputString:
        if char in '({[<':
            S.append(char)
        elif char in ')}]>':
            if len(S) == 0:
                flag = False
                break
            else:
                temp = S.pop()
                if char == '}':
                    if temp in '([<':
                        flag = False
                        break
                    else: cnt += 1
                elif char == ')':
                    if temp in '{[<':
                        flag = False
                        break
                    else: cnt += 1
                elif char == ']':
                    if temp in '{(<':
                        flag = False
                        break
                    else: cnt += 1
                elif char == '>':
                    if temp in '{([':
                        flag = False
                        break
                    else: cnt += 1

    if len(S) != 0 or not flag:
        return -1
    else:
        return cnt

a = [
    'Hello, world!',
    'line [plus]',
    'if (Count of eggs is 4.) {Buy milk.}',
    '>_<',
]
for i in a:
    print(solution(i))



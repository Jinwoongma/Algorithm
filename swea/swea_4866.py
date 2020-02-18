import sys
sys.stdin = open('input_4866.txt', 'r')

TC = int(input())
for tc in range(TC):
    data = str(input())
    S = []
    flag = True

    for char in data:
        if char == '{' or char == '(':
            S.append(char)
        elif char == '}' or char == ')':
            if len(S) == 0:
                flag = False
                break
            else:
                temp = S.pop()
                if char == '}':
                    if temp == '(':
                        flag = False
                        break
                elif char == ')':
                    if temp == '{':
                        flag = False
                        break

    if len(S) != 0 or not flag:
        print('#{} 0'.format(tc + 1))
    else:
        print('#{} 1'.format(tc + 1))
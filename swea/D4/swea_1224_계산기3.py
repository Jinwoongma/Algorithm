import sys
sys.stdin = open('input.txt', 'r')

for tc in range(1, 12):
    N = int(input())
    formular = str(input())
    after = []
    S = []

    for i in range(N):
        if formular[i] == '(': S.append(formular[i])

        elif formular[i] == ')':
            while True:
                if len(S) == 0: break
                temp = S.pop()
                if temp == '(': break
                else: after.append(temp)

        elif formular[i] == '*' or formular[i] == '/':
            if len(S) == 0:
                S.append(formular[i])
                continue
            if S[-1] == '+' or S[-1] == '-' or S[-1] == '(':
                S.append(formular[i])
                continue
            elif S[-1] == '*' or S[-1] == '/':
                while True:
                    if len(S) == 0: break
                    temp = S.pop()
                    if temp == '+' or temp == '-':
                        break
                    elif temp == '*' or temp == '-':
                        after.append(temp)
                        break
                S.append(formular[i])

        elif formular[i] == '+' or formular[i] == '-':
            if len(S) == 0:
                S.append(formular[i])
                continue
            if S[-1] == '(':
                S.append(formular[i])
                continue
            elif S[-1] == '*' or S[-1] == '/' or S[-1] == '+' or S[-1] == '-':
                while True:
                    if len(S) == 0: break
                    temp = S.pop()
                    if temp == '(':
                        break
                    elif temp == '*' or temp == '-' or temp == '+' or temp == '-':
                        after.append(temp)
                        break
                S.append(formular[i])

        else: after.append(int(formular[i]))

        # after += S
        # print(S)
        # print(after)
    print(after)
    S = []
    result = 0
    for i in range(len(after)):
        print(i)
        if after[i] in '+-*/':
            if len(S) < 2:
                print('#{} error'.format(tc + 1))
                break
            num2 = S.pop()
            num1 = S.pop()
            if after[i] == '+': result = int(num1) + int(num2)
            elif after[i] == '-': result = int(num1) - int(num2)
            elif after[i] == '*': result = int(num1) * int(num2)
            elif after[i] == '/': result = int(num1) // int(num2)
            S.append(result)
        elif after[i] == '.':
            if len(S) >= 2:
                print('#{} error'.format(tc + 1))
            else:
                print('#{} {}'.format(tc + 1, S[0]))
        else: S.append(after[i])
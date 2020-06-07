C = int(input())
for tc in range(TC):
    data = list(map(str, input().split()))
    S = []
    for i in range(len(data)):
        if data[i] in '+-*/':
            if len(S) < 2:
                print('#{} error'.format(tc + 1))
                break
            num2 = S.pop()
            num1 = S.pop()
            if data[i] == '+': result = int(num1) + int(num2)
            elif data[i] == '-': result = int(num1) - int(num2)
            elif data[i] == '*': result = int(num1) * int(num2)
            elif data[i] == '/': result = int(num1) // int(num2)
            S.append(result)
        elif data[i] == '.':
            if len(S) >= 2:
                print('#{} error'.format(tc + 1))
            else:
                print('#{} {}'.format(tc + 1, S[0]))
        else: S.append(data[i])
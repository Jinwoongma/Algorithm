TC = int(input())
for tc in range(TC):
    data = input()
    L = len(data)
    for i in range(L // 2):
        if data[i] != data[L - i - 1]:
            if data[i] == '?' or data[L - i - 1] == '?': continue
            else:
                print('#{} Not exist'.format(tc + 1))
                break
    else:
        print('#{} Exist'.format(tc + 1))
TC = int(input())
for tc in range(TC):
    N = int(input())
    data = str(input())
    split_str = [[] for _ in range(N)]
    new_split = []
    print('#{} '.format(tc + 1), end='')
    result = ''
    cnt = 0
    for char in data:
        if char in '!?.':
            split_str[cnt].append(char)
            cnt += 1
            continue
        split_str[cnt].append(char)

    for i in range(N):
        if isinstance(split_str[i], list):
            new_split.append(''.join(split_str[i]))

    for i in range(len(new_split)):
        count = 0
        temp = new_split[i]
        temp2 = temp.lstrip().split()
        for j in range(len(temp2)):
            if len(temp2[j]) == 0:
                continue
            elif len(temp2[j]) == 1 and ord('A') <= ord(temp2[j][0]) <= ord('Z'):
                count += 1
            elif ord('a') <= ord(temp2[j][0]) <= ord('z'):
                continue
            else:
                if ord('A') <= ord(temp2[j][0]) <= ord('Z'):
                    for k in range(1, len(temp2[j])):
                        if ord('A') <= ord(temp2[j][k]) <= ord('Z') or ord('0') <= ord(temp2[j][k]) <= ord('9'):
                            break
                    else:
                        count += 1
                elif j == len(temp2) - 1 and temp2[j][-1] == '.':
                    count += 1
        result += str(count) + ' '
    print(result[:-1])

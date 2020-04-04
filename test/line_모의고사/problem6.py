N, align = map(str, input().split())
N = int(N)
data = []
max_size = -1
length = 0
for i in range(N):
    size, text = map(str, input().split())
    max_size = max(max_size, int(size))
    data.append([int(size), text])
    length += len(text)

result = []
for size, text in data:
    diff = max_size - size
    if align == 'TOP':
        baseline = 0
    elif align == 'MIDDLE':
        baseline = diff
    elif align == 'BOTTOM':
        baseline = diff * 2

    for c in text:
        sub_result = [['.' for _ in range(size)] for _ in range(max_size * 2 - 1)]
        # case 0
        if c == '0':
            for R in range(baseline, baseline + (size * 2 - 1)):
                if R == baseline or R == baseline + (size * 2 - 2):
                    for C in range(size):
                        sub_result[R][C] = '#'
                else:
                    for C in range(size):
                        if C == 0 or C == size - 1:
                            sub_result[R][C] = '#'
        # case 1
        elif c == '1':
            for R in range(baseline, baseline + (size * 2 - 1)):
                for C in range(size):
                    if C == size - 1:
                        sub_result[R][C] = '#'

        # case 2
        elif c == '2':
            for R in range(baseline, baseline + (size * 2 - 1)):
                for C in range(size):
                    if R == baseline or R == baseline + size - 1 or R == baseline + (size * 2 - 2):
                        sub_result[R][C] = '#'
                    elif (R < baseline + size - 1 and C == size - 1) or (baseline + size - 1 < R < baseline + (size * 2 - 2) and C == 0):
                        sub_result[R][C] = '#'

        # case 3
        elif c == '3':
            for R in range(baseline, baseline + (size * 2 - 1)):
                for C in range(size):
                    if R == baseline or R == baseline + size - 1 or R == baseline + (size * 2 - 2):
                        sub_result[R][C] = '#'
                    elif (R < baseline + size - 1 and C == size - 1) or (baseline + size - 1 < R < baseline + (size * 2 - 2) and C == size - 1):
                        sub_result[R][C] = '#'

        # case 4
        elif c == '4':
            for R in range(baseline, baseline + (size * 2 - 1)):
                for C in range(size):
                    if (R < baseline + size - 1) and (C == 0 or C == size - 1):
                        sub_result[R][C] = '#'
                    elif R == baseline + size - 1:
                        sub_result[R][C] = '#'
                    elif (R > baseline + size - 1) and (C == size - 1):
                        sub_result[R][C] = '#'

        # case 5
        elif c == '5':
            for R in range(baseline, baseline + (size * 2 - 1)):
                for C in range(size):
                    if R == baseline or R == baseline + size - 1 or R == baseline + (size * 2 - 2):
                        sub_result[R][C] = '#'
                    elif (R < baseline + size - 1 and C == 0) or (
                            baseline + size - 1 < R < baseline + (size * 2 - 2) and C == size - 1):
                        sub_result[R][C] = '#'

        # case 6
        elif c == '6':
            for R in range(baseline, baseline + (size * 2 - 1)):
                for C in range(size):
                    if (R < baseline + size - 1) and (C == 0):
                        sub_result[R][C] = '#'
                    elif (R == baseline + size - 1) or (R == baseline + (size * 2 - 2)):
                        sub_result[R][C] = '#'
                    elif (baseline + size - 1 < R < baseline + (size * 2 - 2)) and (C == 0 or C == size - 1):
                        sub_result[R][C] = '#'

        # case 7
        elif c == '7':
            for R in range(baseline, baseline + (size * 2 - 1)):
                for C in range(size):
                    if C == size - 1:
                        sub_result[R][C] = '#'
                    elif R == baseline:
                        sub_result[R][C] = '#'

        # case 8
        elif c == '8':
            for R in range(baseline, baseline + (size * 2 - 1)):
                if R == baseline or R == baseline + size - 1 or R == baseline + (size * 2 - 2):
                    for C in range(size):
                        sub_result[R][C] = '#'
                else:
                    for C in range(size):
                        if C == 0 or C == size - 1:
                            sub_result[R][C] = '#'

        # case 9
        elif c == '9':
            for R in range(baseline, baseline + (size * 2 - 1)):
                for C in range(size):
                    if (R > baseline + size - 1) and (C == size - 1):
                        sub_result[R][C] = '#'
                    elif (R == baseline + size - 1) or (R == 0):
                        sub_result[R][C] = '#'
                    elif (baseline <= R < baseline + size - 1) and (C == 0 or C == size - 1):
                        sub_result[R][C] = '#'

        result.append(sub_result)

# result[index][y][x]
temp = []
for R in range(max_size * 2 - 1):
    temp2 = []
    for idx in range(length):
        temp2.append(result[idx][R])
        temp2.append([' '])

    str_temp = ''
    for i in range(len(temp2)):
        str_temp += ''.join(temp2[i])
    print(str_temp[:-1])

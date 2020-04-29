def Binary(num):
    global result
    mok, nam = 0, 0
    for i in range(4):
        mok = num // 2
        nam = num % 2
        result = str(nam) + result
        num = mok
    return


T = int(input())
Conversion = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
              'D': 13, 'E': 14, 'F': 15}
for t in range(T):
    N, input_num = map(str, input().split())
    final_result = ''
    for i in input_num:
        result = ''
        decimal_num = Conversion[i]
        Binary(decimal_num)
        final_result += result
    print("#%d %s" % (t + 1, final_result))
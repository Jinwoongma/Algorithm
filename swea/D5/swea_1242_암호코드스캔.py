hcode = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
         '4':'0100', '5':'0101', '6':'0110', '7':'0111',
         '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
         'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

scode = {211:0, 221:1, 122:2, 411:3, 132:4, 231:5, 114:6, 312:7, 213:8, 112:9}

TC = int(input())
for tc in range(TC):
    R, C = map(int, input().split())
    data = [input() for _ in range(R)]
    answer = 0

    mat = [''] * R
    for i in range(R):
        for j in range(C):
            mat[i] += hcode[data[i][j]]

    for i in range(1, len(mat) - 6):
        j = C * 4 - 1
        while j > 56:
            if mat[i][j] == '1' and mat[i - 1][j] == '0':
                c = [0] * 8
                for k in range(7, -1, -1):
                    c1, c2, c3 = 0, 0, 0
                    while mat[i][j] == '1': c3 += 1; j -= 1
                    while mat[i][j] == '0': c2 += 1; j -= 1
                    while mat[i][j] == '1': c1 += 1; j -= 1
                    while mat[i][j] == '0' and k: j -= 1

                    MIN = min(c1, c2, c3)
                    c1, c2, c3 = c1 // MIN, c2 // MIN, c3 // MIN
                    c[k] = scode[100 * c1 + 10 * c2 + c3]

                t = 3 * (c[0] + c[2] + c[4] + c[6]) + c[1] + c[3] + c[5] + c[7]
                if t % 10 == 0:
                    answer += sum(c)
            j -= 1
    print('#{} {}'.format(tc + 1, answer))

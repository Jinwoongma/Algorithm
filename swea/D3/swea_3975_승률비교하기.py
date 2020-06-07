TC = int(input())
result = []
for tc in range(TC):
    a_win, a_all, b_win, b_all = map(int, input().split())
    if float(a_win / a_all) > float(b_win / b_all):
        result.append('ALICE')
    elif float(a_win / a_all) < float(b_win / b_all):
        result.append('BOB')
    else:
        result.append('DRAW')

for tc in range(TC):
    print('#{} {}'.format(tc+1, result[tc]))

omok = [list(map(int, input().split())) for _ in range(19)]
flag = False
for i in range(19):
    for j in range(19):
        # 오른쪽 체크
        if j >= 15:
            continue
        else:
            if omok[i][j] == 1:
                for k in range(j+1, j+5):
                    if omok[i][k] != 1:
                        break
                else:
                    if j == 0:
                        if omok[i][j+5] == 1:
                            break
                        else:
                            print('1')
                            print(i + 1, j + 1)
                            break
                    elif j == 14:
                        if omok[i][j-1] == 1:
                            break
                        else:
                            print('1')
                            print(i + 1, j + 1)
                            break
                    else:
                        if omok[i][j-1] == 1 or omok[i][j+5] == 1:
                            break
                        else:
                            print('1')
                            print(i + 1, j + 1)
                            break

            elif omok[i][j] == 2:
                for k in range(j+1, j+5):
                    if omok[i][k] != 2:
                        break
                else:
                    if j == 0:
                        if omok[i][j+5] == 2:
                            break
                        else:
                            print('2')
                            print(i + 1, j + 1)
                            break
                    elif j == 14:
                        if omok[i][j-1] == 2:
                            break
                        else:
                            print('2')
                            print(i + 1, j + 1)
                            break
                    else:
                        if omok[i][j-1] == 2 or omok[i][j+5] == 2:
                            break
                        else:
                            print('2')
                            print(i + 1, j + 1)
                            break

        # 아래 체크
        if i >= 15:
            continue
        else:
            if omok[i][j] == 1:
                for k in range(i + 1, i + 5):
                    if omok[k][j] != 1:
                        break
                else:
                    if i == 0:
                        if omok[i + 5][j] == 1:
                            break
                        else:
                            print('1')
                            print(i + 1, j + 1)
                            break
                    elif i == 14:
                        if omok[i - 1][j] == 1:
                            break
                        else:
                            print('1')
                            print(i + 1, j + 1)
                            break
                    else:
                        if omok[i - 1][j] == 1 or omok[i + 5][j] == 1:
                            break
                        else:
                            print('1')
                            print(i + 1, j + 1)
                            break

            elif omok[i][j] == 2:
                for k in range(i + 1, i + 5):
                    if omok[k][j] != 2:
                        break
                else:
                    if i == 0:
                        if omok[i + 5][j] == 2:
                            break
                        else:
                            print('2')
                            print(i + 1, j + 1)
                            break
                    elif j == 14:
                        if omok[i - 1][j] == 2:
                            break
                        else:
                            print('2')
                            print(i + 1, j + 1)
                            break
                    else:
                        if omok[i - 1][j] == 2 or omok[i + 5][j] == 2:
                            break
                        else:
                            print('2')
                            print(i + 1, j + 1)
                            break

        # 오른 아래 대각선 체크
        if i >= 15 or j >= 15:
            continue
        else:
            if omok[i][j] == 1:
                for k in range(1, 5):
                    if omok[i + k][j + k] != 1:
                        break
                else:
                    if i == 0 and j == 14:
                        print('1')
                        print(i + 1, j + 1)
                        break
                    if i == 0 or j == 0:
                        if omok[i + 5][j + 5] == 1:
                            break
                        else:
                            print('1')
                            print(i + 1, j + 1)
                            break
                    elif i == 14 or j == 14:
                        if omok[i - 1][j - 1] == 1:
                            break
                        else:
                            print('1')
                            print(i + 1, j + 1)
                            break
                    else:
                        if omok[i - 1][j - 1] == 1 or omok[i + 5][j + 5] == 1:
                            break
                        else:
                            print('1')
                            print(i + 1, j + 1)
                            break

            elif omok[i][j] == 2:
                for k in range(1, 5):
                    if omok[i+k][j+k] != 2:
                        break
                else:
                    if i == 0 and j == 14:
                        print('2')
                        print(i + 1, j + 1)
                        break
                    if i == 0 or j == 0:
                        if omok[i + 5][j + 5] == 2:
                            break
                        else:
                            print('2')
                            print(i + 1, j + 1)
                            break
                    elif j == 14 or i == 14:
                        if omok[i - 1][j - 1] == 2:
                            break
                        else:
                            print('2')
                            print(i + 1, j + 1)
                            break
                    else:
                        if omok[i - 1][j - 1] == 2 or omok[i + 5][j + 5] == 2:
                            break
                        else:
                            print('2')
                            print(i + 1, j + 1)
                            break

        # 왼쪽 아래 대각선 체크
        if i >= 15 or j <= 3:
            continue
        else:
            if omok[i][j] == 1:
                for k in range(1, 5):
                    if omok[i + k][j - k] != 1:
                        break
                else:
                    if i == 0 and j == 4:
                        print('1')
                        print(i + 1, j + 1)
                        break
                    if i == 0 or j == 18:

                        if omok[i + 5][j - 5] == 1:
                            break
                        else:
                            print('1')
                            print(i + 1, j + 1)
                            break
                    elif i == 14 or j == 14:
                        if omok[i - 1][j + 1] == 1:
                            break
                        else:
                            print('1')
                            print(i + 1, j + 1)
                            break
                    else:
                        if omok[i + 1][j + 1] == 1 or omok[i + 5][j - 5] == 1:
                            break
                        else:
                            print('1')
                            print(i + 1, j + 1)
                            break

            elif omok[i][j] == 2:
                for k in range(1, 5):
                    if omok[i + k][j - k] != 2:
                        break
                else:
                    if i == 0 and j == 4:
                        print('2')
                        print(i + 1, j + 1)
                        break
                    if i == 0 or j == 18:
                        print('!')
                        if omok[i + 5][j - 5] == 2:
                            break
                        else:
                            print('2')
                            print(i + 1, j + 1)
                            break
                    elif i == 14 or j == 14:
                        if omok[i - 1][j + 1] == 2:
                            break
                        else:
                            print('2')
                            print(i + 1, j + 1)
                            break
                    else:
                        if omok[i + 1][j + 1] == 2 or omok[i + 5][j - 5] == 2:
                            break
                        else:
                            print('2')
                            print(i + 1, j + 1)
                            break

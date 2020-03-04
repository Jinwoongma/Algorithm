from _collections import deque

def get_score(arr):
    cnt, flag5, flag10, flag15 = arr
    print(arr)
    if not flag5 and not flag10 and not flag15:
        if cnt == 5:
            arr[1] = True
        elif cnt == 10:
            arr[2] = True
        elif cnt == 15:
            arr[3] = True

        if cnt >= len(line1):
            arr[0] = -1
            return arr, -1
        else:
            return arr, line1[cnt]

    if not flag5 and not flag10 and flag15:
        if cnt >= len(line2):
            arr[0] = -1
            return arr, -1
        else:
            return arr, line2[cnt]

    if not flag5 and flag10 and not flag15:
        if cnt >= len(line3):
            arr[0] = -1
            return arr, -1
        else:
            return arr, line3[cnt]

    if flag5 and not flag10 and not flag15:
        if cnt >= len(line4):
            arr[0] = -1
            return arr, -1
        else:
            return arr, line4[cnt]


def dfs(m, turn, mal_cnt, score, path, score_path):
    global max_score, max_path, max_spath
    if turn == 10:
        if score > max_score:
            max_score = score
            max_path = path
            max_spath = score_path
        return

    if mal_cnt != 4:
        for i in range(mal_cnt):
            if m[i][0] == -1: continue
            m[i][0] += num[turn]
            temp_m, temp_score = get_score(m[i])
            if temp_score == -1:
                return
            else:
                new_score, m[i] = score + temp_score, temp_m
            dfs(m, turn + 1, mal_cnt, new_score, path + [i], score_path + [temp_score])

        m[mal_cnt][0] += num[turn]
        temp_m, temp_score = get_score(m[mal_cnt])
        if temp_score == -1:
            return
        else:
            new_score, m[mal_cnt] = score + temp_score, temp_m
        dfs(m, turn + 1, mal_cnt + 1, new_score, path + [mal_cnt], score_path + [temp_score])
    else:
        for i in range(4):
            if m[i][0] == -1: continue
            temp_m, temp_score = get_score(m[i])
            if temp_score == -1:
                return
            else:
                new_score, m[i] = score + temp_score, temp_m
            dfs(m, turn + 1, mal_cnt, new_score, path + [i], score_path + [temp_score])




num = list(map(int, input().split()))
m = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
line1 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40]
line2 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 27, 26, 25, 30, 35, 40]
line3 = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30, 35, 40]
line4 = [0, 2, 4, 6, 8, 10, 13, 16, 19, 25, 30, 35, 40]
max_score, max_path, max_spath = -1, [], []

dfs(m, 0, 1, 0, [], [])
print(max_score)
print(max_path)
print(max_spath)
def solution(road, n):
    answer = -1
    zero_cnt = 0
    line_cnt = 0
    temp = ''
    MAX = 0
    for i in range(len(road)):
        if road[i] == '1':
            temp += road[i]
            line_cnt += 1
        else:
            if zero_cnt < n:
                zero_cnt += 1
                temp += road[i]
            else:
                for j in range(len(temp)):
                    if temp[j] == '0':
                        temp = temp[j + 1:]
                        break
                temp += road[i]
        MAX = max(MAX, len(temp))
    return MAX

print(solution("001100", 5))
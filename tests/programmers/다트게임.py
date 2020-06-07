def solution(dartResult):
    answer = 0
    results = []
    temp = ''
    i = 0
    while True:
        if i >= (len(dartResult)):
            results.append(temp)
            break
        if ord('0') <= ord(dartResult[i]) <= ord('9'):
            if temp == '' or temp == '1':
                temp += dartResult[i]
            else:
                results.append(temp)
                temp = dartResult[i]
        else:
            temp += dartResult[i]
        i += 1
    print(results)

    score_list = [0] * len(results)
    for i in range(len(results)):
        if results[i][:2] == '10':
            score, bonus = int(results[i][:2]), results[i][2]
        else:
            score, bonus = int(results[i][0]), results[i][1]
        if bonus == 'D':
            score = score ** 2
        elif bonus == 'T':
            score = score ** 3
        score_list[i] = score

        if results[i][-1] == '#' or results[i][-1] == '*':
            if results[i][-1] == '*':
                if i == 0:
                    score_list[i] *= 2
                else:
                    score_list[i] *= 2
                    score_list[i - 1] *= 2
            else:
                score_list[i] *= -1
    print(score_list)
    return sum(score_list)

dartResult = [
    '1S2D*3T',
    '1D2S#10S',
    '1D2S0T',
    '1S*2T*3S',
    '1D#2S*3S',
    '1T2D3D#',
    '1D2S3T*',
]

for i in dartResult:
    print(solution(i))
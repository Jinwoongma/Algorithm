def solution(answer_sheet, sheets):
    answer = -1
    for i in range(len(sheets)):
        for j in range(len(sheets)):
            if j <= i: continue
            doubt = 0
            cnt = 0
            continuity = 0
            flag = False
            for k in range(len(answer_sheet)):
                if sheets[i][k] != sheets[j][k]:
                    flag = False
                    cnt = 0
                    continue  # 문제 답이 다를 떄
                if answer_sheet[k] != sheets[i][k]:  # 문제도 틀리고 답이 같을 때
                    if flag:
                        cnt += 1
                        doubt += 1
                    else:
                        doubt += 1
                        cnt = 1
                        flag = True
                else:
                    flag = False
                    cnt = 0
                continuity = max(continuity, cnt)
            answer = max(answer, doubt + (continuity ** 2))
    return answer

a = ['4132315142',
     "53241",
     "24551"
     ]

b = [["3241523133","4121314445","3243523133","4433325251","2412313253"],
     ["53241", "42133", "53241", "14354"],
     ["24553", "24553", "24553", "24553"]
     ]

for i in range(3):
    print(solution(a[i], b[i]))
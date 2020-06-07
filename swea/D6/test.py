def solution(s):
    lst = s.split()
    answer = ''
    for j in range(len(lst)):
        print(lst[j])
        lst[j] = lst[j].capitalize()
        answer += lst[j] + ' '

    return answer[:-1]

print(solution('   '))
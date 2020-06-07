def solution(ip_addrs, langs, scores):
    N = len(ip_addrs)
    answer = N
    memo = {}
    for i in range(N):
        ip, lang, score = ip_addrs[i], langs[i], scores[i]
        if lang == 'C++' or lang == 'C#': lang = 'C'
        if ip not in memo:
            memo[ip] = [[lang, score]]
        else:
            memo[ip].append([lang, score])

    for key, val in memo.items():
        print(key, val, len(val))
        if len(val) == 2:
            if val[0][0] == val[1][0] and val[0][1] == val[1][1]:
                answer -= 2
        elif len(val) == 3:
            if val[0][0] == val[1][0] and val[1][0] == val[2][0] and val[0][0] == val[2][0]:
                answer -= 3
        elif len(val) >= 4:
            answer -= len(val)
    return answer


a = [["5.5.5.5", "155.123.124.111", "10.16.125.0", "155.123.124.111", "5.5.5.5", "155.123.124.111", "10.16.125.0", "10.16.125.0"],
     ["Java", "C++", "Python3", "C#", "Java", "C", "Python3", "JavaScript"],
     [294, 197, 373, 45, 294, 62, 373, 373]]


print(solution(a[0], a[1], a[2]))
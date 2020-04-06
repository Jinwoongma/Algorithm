def solution(s):
    if len(s) == 1:
        return 1
    else:
        answer = 0xfffff
        for i in range(1, len(s) // 2 + 1):
            result = ''
            index = 0
            while True:
                if index + i > len(s):
                    result += s[index:]
                    break

                if s[index:index + i] != s[index + i:index + (2 * i)]:
                    result += s[index:index + i]
                    index += i
                    continue
                else:
                    ref = s[index:index + i]
                    cnt = 2
                    while True:
                        if index + (i * (cnt + 1)) > len(s) or ref != s[index + (i * cnt):index + (i * (cnt + 1))]:
                            break
                        cnt += 1
                    result += str(cnt) + ref
                    index += cnt * i
            answer = min(answer, len(result))

    return answer


print(solution('a'))
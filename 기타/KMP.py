def getpartialmatch(N):
    #  N에서 자기 자신을 찾으면서 나타나는 부분일치를 이용해 pi[]를 계산한다
    m = len(N)
    pi = [0] * m
    begin, match = 1, 0  #  begin = 0이면 자신을 찾아버리니까 안됨
    # 비교할 문자가 N의 끝에 도달할 떄까지 찾으면서 부분일치를 모두 기록한다
    while begin + match < m:
        if N[begin + match] == N[match]:
            match += 1
            pi[begin + match - 1] = match
        else:
            if match == 0:
                begin += 1
            else:
                begin += match - pi[match - 1]
                match = pi[match - 1]
    return pi


def KMP(H, N):
    result = []
    n, m = len(H), len(N)
    begin, match = 0, 0
    pi = getpartialmatch(N)
    while begin < n - m:
        if match < m and H[begin + match] == N[match]:
            match += 1
            if match == m:
                result.append(begin)
        else:
            if match == 0:
                begin += 1
            else:
                begin += match - pi[match - 1]
                match = pi[match - 1]
    return result


print(KMP('pipipipip', 'pi'))
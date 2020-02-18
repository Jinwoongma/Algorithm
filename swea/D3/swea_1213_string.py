import sys
sys.stdin = open('input_1213.txt', 'r', encoding='UTF8')

def getpartialmatch(N):
    m = len(N)
    pi = [0] * m
    begin, matched = 1, 0
    while begin + matched < m:
        if N[begin + matched] == N[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return pi

def KMP(H, N):
    pi = getpartialmatch(N)
    n, m = len(H), len(N)
    begin, matched = 0, 0
    result = []
    while begin <= n - m:
        if matched < m and H[begin + matched] == N[matched]:
            matched += 1
            if matched == m:
                result.append(begin)
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched - 1]
                matched = pi[matched - 1]
    return result


for tc in range(10):
    t = int(input())
    N = input()
    H = input()

    print('#{} {}'.format(tc + 1, len(KMP(H, N))))
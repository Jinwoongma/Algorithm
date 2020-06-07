def fight(ind1, ind2):
    if cards[ind1] == 1 and cards[ind2] == 2: return ind2
    elif cards[ind1] == 1 and cards[ind2] == 3: return ind1
    elif cards[ind1] == 2 and cards[ind2] == 1: return ind1
    elif cards[ind1] == 2 and cards[ind2] == 3: return ind2
    elif cards[ind1] == 3 and cards[ind2] == 1: return ind2
    elif cards[ind1] == 3 and cards[ind2] == 2: return ind1
    elif cards[ind1] == cards[ind2]: return min(ind1, ind2)

def solution(lo, hi):
    if lo == hi:
        return lo

    mid = (lo + hi) >> 1
    l = solution(lo, mid)
    r = solution(mid + 1, hi)
    return fight(l, r)

TC = int(input())
for tc in range(TC):
    N = int(input())
    cards = list(map(int, input().split()))
    print('#{} {}'.format(tc + 1, solution(0, N - 1) + 1))
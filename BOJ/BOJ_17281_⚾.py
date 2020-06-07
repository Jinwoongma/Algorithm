# https://inspirit941.tistory.com/entry/Python-%EB%B0%B1%EC%A4%80-17281-%E2%9A%BE
# 이 문제는 순열을 짤때 재귀형식으로 짜면 무조건 tle 이다
# 왜냐하면 permutations 는 c 로 작동하는 데 반해, 재귀형식으로 짜면 온전히 파이썬으로 작동하기 때문에 tle
# ---- Type Your Code Here ---- #

from itertools import permutations

def game(arr):
    score = 0
    num = 1
    for inning in range(1, N + 1):
        r1, r2, r3 = 0, 0, 0
        out = 0
        while True:
            if out == 3:
                break
            p = P[inning][arr[num]]
            if p == 0:
                out += 1

            elif p == 1:
                score += r3
                r1, r2, r3 = 1, r1, r2

            elif p == 2:
                score += r2 + r3
                r1, r2, r3 = 0, 1, r1

            elif p == 3:
                score += r1 + r2 + r3
                r1, r2, r3 = 0, 0, 1

            elif p == 4:
                score += r1 + r2 + r3 + 1
                r1, r2, r3 = 0, 0, 0

            if num == 9: num = 1
            else: num += 1

    return score


N = int(input())
P = [[0] * 9] + [[0] + list(map(int, input().split())) for _ in range(N)]
max_score = -1

for perm in permutations(range(2, 10)):
    arr = [0] + list(perm)[:3] + [1] + list(perm)[3:]
    score = game(arr)
    if score > max_score:
        max_score = score

print(max_score)
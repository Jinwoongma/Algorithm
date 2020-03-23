import sys
from itertools import combinations

N, K = map(int, input().split())
check = [[] for _ in range(N + 1)]
base = 'antic'
result = -1
if K >= 5:
    need = set()
    for i in range(N):
        temp = str(input())[4:-4]
        for c in temp:
            if c not in base:
                check[i + 1].append(c)
                need.add(c)
    need = list(need)

    if len(need) < K - 5:
        result = N
    else:
        for perms in combinations(need, K - 5):
            sub_result = 0
            for i in range(1, N + 1):
                flag = True
                for j in range(len(check[i])):
                    if check[i][j] not in perms:
                        flag = False
                        break
                if flag:
                    sub_result += 1

            result = max(result, sub_result)

    if result == -1:
        print(0)
    else:
        print(result)
else:
    print(0)
    sys.exit(0)

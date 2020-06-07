def solve(k):
    global answer
    if k == N:
        answer = max(answer, int(''.join(num_list)))
        return
    for i in range(len(num_list) - 1):
        for j in range(i + 1, len(num_list)):
            num_list[i], num_list[j] = num_list[j], num_list[i]

            res = int(''.join(num_list))
            if res not in visited[k + 1]:
                visited[k + 1].add(res)
                solve(k + 1)

            num_list[i], num_list[j] = num_list[j], num_list[i]


TC = int(input())
for tc in range(TC):
    num, N = map(int, input().split())
    num_list = list(str(num))
    visited = [set() for _ in range(N + 1)]
    answer = 0
    solve(0)
    print('#{} {}'.format(tc + 1, answer))
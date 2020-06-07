from copy import deepcopy

# 1. n개의 사탕을 r 명의 아이들에게 나누는 조합 (n C r) 생성
# 2. 생성된 조합 순서로 r명의 아이들에게 사탕을 나눠 준다.
# 3. 나눠준 후 아이들이 갖고있는 사탕 종류의 합을 계산하고 최대값(answer)을 갱신한다.
def solve(depth):
    global answer
    if depth == r:
        new_candy = deepcopy(candy) # new_candy: 사탕을 추가로 나눠준 결과를 저장하는 리스트
        SUM = 0  # 아이들이 지닌 사탕 종류 개수의 합을 저장하는 변수
        for i in range(r):
            new_candy[i].add(arr[i])
            SUM += len(new_candy[i])
        answer = max(answer, SUM) 
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            arr.append(i + 1)
            solve(depth + 1)
            arr.pop()
            visited[i] = False


TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())

    # candy: i 번째 아이가 가지고 있는 사탕의 종류를 저장하는 배열
    # ex) [{1, 2, 3}, {1}, {2, 3}, {2}] -> 0 번째 아이는 1, 2, 3 사탕을 갖고 있음
    candy = []
    for i in range(N):
        candy.append(set(list(map(int, input().split()))[1:]))

    # n, r 전처리: 아이들 수(M)가 사탕 종류(N)보다 많을 경우 나눠줄 아이들 수(r)를 N 으로 변경
    if M > N:
        n, r = N, N
    else:
        n, r = N, M

    # visited: 조합을 생성하기 위한 방문처리 리스트
    # arr: 생성된 조합을 저장하기 위한 리스트
    # answer: 최대값을 저장하는 변수(-1 로 초기화)
    visited = [False for _ in range(n)]
    arr = []
    answer = -1
    
    # 문제 해결 함수
    solve(0)

    print('#{} {}'.format(tc + 1, answer))
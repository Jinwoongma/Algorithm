arr = 'ABC'
N = len(arr)
visit = [0] * N  # 순열 생성하기 위해 선택된 요소들의 정보

def backtrack(k):  # k: 함수 호출의 깊이, 지금까지 선택된 요소의 수
    if k == N:  # 단말노드에 도착, 모든 선택이 완료된 상태
        print(order)

    else:  # 아직 해야할 선택이 남은 상태
        for i in range(N):
            if visit[i]: continue
            visit[i] = 1
            order.append(arr[i])
            backtrack(k + 1)
            visit[i] = 0
            order.pop()
order = []
backtrack(0)
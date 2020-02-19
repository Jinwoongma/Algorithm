arr = 'ABC'
N = len(arr)

def backtrack(k):  # k: 함수 호출의 깊이, 지금까지 선택된 요소의 수
    if k == N:  # 단말노드에 도착, 모든 선택이 완료된 상태
        print(order)
    else:  # 아직 해야할 선택이 남은 상태
        for i in range(N):
            order.append(arr[i])
            backtrack(k + 1)
            order.pop()

order = []
backtrack(0)
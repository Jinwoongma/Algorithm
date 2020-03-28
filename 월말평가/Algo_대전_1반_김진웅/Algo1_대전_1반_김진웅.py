TC = int(input())
for tc in range(TC):
    N = int(input())
    A = list(map(int, input().split()))

    for rep in range(N):
        new_A = [[] for _ in range(10)]  # 옮겨진 값들을 저장할 새로운 배열 생성
        for i in range(len(A)):
            if abs(A[i]) >= 10:  # A[i]의 절대값이 10이상일 때
                a, b = -1 * (abs(A[i]) // 2), abs(A[i]) // 2
                if i + 1 >= 10 and A[i] > 0:  # 맨 끝에 위치해있고, A[i]가 양수일 때
                    new_A[i - 1].append(a)    # 첫번째 수는 끝에서 두번째 인덱스에,
                    new_A[i].append(b * -1)   # 두번쨰 수는 부호를 바꿔 마지막 인덱스에 위치

                elif i - 1 < 0 and A[i] < 0:  # 맨 처음에 위치해있고, A[i]가 음수일 때
                    new_A[i].append(a * -1)   # 첫번째 수는 부호를 바꿔 첫번째 인덱스에,
                    new_A[i + 1].append(b)    # 두번째 수는 두번째 인덱스에 위치

                else:                         # 위의 두가지 경우가 아닐 때
                    new_A[i - 1].append(a)    # 첫번쨰 수는 바로 왼쪽에 위치
                    new_A[i + 1].append(b)    # 두번째 수는 바로 오른쪽에 위치

            else:  # A[i]의 절대값이 10미만일 때
                if A[i] > 0:                        # A[i]가 양수일 때
                    if i + 1 >= 10:                 # 맨 마지막 인덱스일 떄
                        new_A[i].append(-1 * A[i])  # 부호를 바꿔 마지막 인덱스에 위치
                    else:                           # 마지막 인덱스가 아닐 떄
                        new_A[i + 1].append(A[i])   # 숫자 그대로 오른쪽 인덱스에 위치

                if A[i] < 0:                        # A[i]가 음수일 때
                    if i - 1 < 0:                   # 맨 처음 인덱스일 떄
                        new_A[i].append(-1 * A[i])  # 부호를 바꿔 처음 인덱스에 위치
                    else:                           # 맨 처음 인덱스가 아닐 떄
                        new_A[i - 1].append(A[i])   # 숫자 그대로 왼쪽 인덱스에 위치

        A = [sum(idx) for idx in new_A]  # 옮겨진 수들의 합이 계산된 새로운 배열 A 생성

    print('#{} {}'.format(tc + 1, ' '.join(map(str, A))))
from collections import deque


def solution(progresses, speeds):
    answer = []
    p = deque(progresses)

    while p:
        for i in range(len(p)):
            if p[i] >= 100: continue
            p[i] += speeds[i]

        if p[0] >= 100:
            cnt = 0
            while p and p[0] >= 100:
                print(cnt)
                cnt += 1
                p.popleft()
            answer.append(cnt)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
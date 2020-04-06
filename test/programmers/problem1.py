import heapq
def solution(jobs):
    answer = 0
    h = []
    cur, end, cnt = 0, -1, 0
    while cnt < len(jobs):
        for i in range(len(jobs)):
            if end < jobs[i][0] <= cur:
                waiting = cur - jobs[i][0]
                answer += waiting
                heapq.heappush(h, jobs[i][1])
        if len(h) > 0:
            answer += len(h) * h[0]
            end = cur
            cur += heapq.heappop(h)
            cnt += 1
        else:
            cur += 1

    return answer // len(jobs)

jobs = [[0, 3], [1, 9], [2, 6]]

print(solution(jobs))
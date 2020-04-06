import heapq
def solution(n, times):
    h = []
    for i in times:
        heapq.heappush(h, (0, i))

    for i in range(n):
        cur, val = heapq.heappop(h)
        heapq.heappush(h, (cur + val, val))

        print(h)
    return answer

solution(6, [7, 10])
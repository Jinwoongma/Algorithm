import heapq

N, K = map(int, input().split())
h = []
for i in range(1, K + 1):
    heapq.heappush(h, (0, i))

for i in range(N):
    cur, idx = heapq.heappop(h)
    cur += int(input())
    heapq.heappush(h, (cur, idx))

ans = -1
for val, idx in h:
    ans = max(ans, val)
print(ans)

###########################################

def minTicketOffice():
    MIN = ticketOffice[0]
    index = 0
    for i in range(K):
        if MIN > ticketOffice[i]:
            MIN = ticketOffice[i]
            index = i
    return index


N, K = map(int, input().split())
group = []
ticketOffice = [0] * 20
maxVisitor = 0

for i in range(N):
    group.append(int(input()))

for i in range(N):
    tempIndex = minTicketOffice()
    ticketOffice[tempIndex] += group[i]
    maxVisitor = max(maxVisitor, ticketOffice[tempIndex])

print(maxVisitor)

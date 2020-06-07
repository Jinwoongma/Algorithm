from collections import deque
TC = int(input())
for tc in range(TC):
    data = list(map(str, input().strip()))
    left, right = [], deque()
    cur = 0
    for i in range(len(data)):
        if data[i] == '<':
            if len(left) > 0:
                right.appendleft(left.pop())
        elif data[i] == '>':
            if len(right) > 0:
                left.append(right.popleft())
        elif data[i] == '-':
            if len(left) > 0:
                left.pop()
        else:
            left.append(data[i])
    print(''.join(left + list(right)))
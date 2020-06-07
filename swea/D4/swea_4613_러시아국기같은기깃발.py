import sys
sys.stdin = open('input_4613.txt', 'r')

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]

    arr = []
    for i in range(1, N - 1):
        for j in range(1, N - 1):
            for k in range(1, N - 1):
                if i + j + k == N:
                    arr.append([i, j, k])

    for i in range(len(arr)):
        line = 0
        temp = [(0, arr[i][0])]
        for i in range(1, 3):
            temp.append((arr[i - 1][1], arr[i - 1][0] + arr[i][0]))
        print(temp)
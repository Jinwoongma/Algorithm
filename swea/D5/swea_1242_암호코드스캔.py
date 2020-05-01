TC = int(input())
for tc in range(TC):
    R, C = map(int, input().split())
    data = [input() for _ in range(R)]
    print(data)

    for i in range(R):
        for j in range(C):
            S = []
            if data[i][j] != 0:


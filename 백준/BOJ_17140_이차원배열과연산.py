r, c, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(3)]
row, col = 3, 3
time = 0

while True:
    if r <= row and c <= col:
        if data[r - 1][c - 1] == k:
            print(time)
            break
    if time > 100:
        print(-1)
        break

    # R 연산
    if row >= col:
        entire = []
        max_length = -1
        for i in range(row):
            temp = []
            count = {}
            length = 0
            for j in range(col):
                if data[i][j] == 0: continue
                if data[i][j] not in count:
                    count[data[i][j]] = 1
                    length += 1
                else:
                    count[data[i][j]] += 1
            max_length = max(max_length, length)

            for key, val in count.items():
                temp.append((key, val))
            temp.sort(key=lambda x: (x[1], x[0]))
            entire.append(temp)

        new_data = [[0 for _ in range(max_length * 2)] for _ in range(row)]
        for i in range(len(entire)):
            diff = max_length - len(entire[i])
            temp = []
            for j in range(len(entire[i])):
                if j * 2 <= 100:
                    new_data[i][j * 2] = entire[i][j][0]
                if j * 2 + 1 <= 100:
                    new_data[i][j * 2 + 1] = entire[i][j][1]

        col = max_length * 2
        data = new_data

    # C 연산
    else:
        entire = []
        max_length = -1
        for i in range(col):
            temp = []
            count = {}
            length = 0
            for j in range(row):
                if data[j][i] == 0: continue
                if data[j][i] not in count:
                    count[data[j][i]] = 1
                    length += 1
                else:
                    count[data[j][i]] += 1

            max_length = max(max_length, length)

            for key, val in count.items():
                temp.append((key, val))
            temp.sort(key=lambda x: (x[1], x[0]))
            entire.append(temp)

        new_data = [[0 for _ in range(col)] for _ in range(max_length * 2)]
        for i in range(len(entire)):
            diff = max_length - len(entire[i])
            temp = []
            for j in range(len(entire[i])):
                if j * 2 <= 100:
                    new_data[j * 2][i] = entire[i][j][0]
                if j * 2 + 1 <= 100:
                    new_data[j * 2 + 1][i] = entire[i][j][1]
        row = max_length * 2
        data = new_data

    time += 1

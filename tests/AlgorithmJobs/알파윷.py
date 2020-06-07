MAP = [0 for _ in range(31)]
turn = [0 for _ in range(31)]
score = [0, 5, 10, 15, 20, 50, 30, 35, 40, 45, 100,
         55, 60, 65, 70, 75, 80, 85, 90, 95, 500,
         1000, 275, 250, 300, 350, 400, 175, 150, 150, 125]
for i in range(21):
    MAP[i] = i + 1
MAP[21] = 21
for i in range(22, 26):
    MAP[i] = i + 1
MAP[26] = 20; MAP[27] = 15; MAP[28] = 27
MAP[29] = 30; MAP[30] = 24; MAP[24] = 28
turn[5] = 22; turn[10] = 29; turn[15] = 16; turn[24] = 25
temp = [24, 25, 26, 20, 21]


def solve(index):
    global answer
    if index == 10:
        SUM = 0
        for i in range(4):
            SUM += score[mal[i]]
        answer = max(answer, SUM)
        return
    for i in range(4):
        prev = mal[i]
        now = prev
        move = data[index]
        if now == 21: continue

        if turn[now] > 0:
            now = turn[now]
            move -= 1

        while move:
            if now == 30:
                now = temp[move - 1]
                break
            now = MAP[now]
            move -= 1

        if now != 21 and visited[now]: continue  # 이미 말이 있으면 pass

        visited[now] = True
        visited[prev] = False
        mal[i] = now
        solve(index + 1)
        mal[i] = prev
        visited[now] = False
        visited[prev] = True


TC = int(input())
for tc in range(TC):
    data = list(map(int, input().split()))
    visited = [False for _ in range(31)]
    mal = [0 for _ in range(4)]
    answer = -1
    solve(0)
    print('#{} {}'.format(tc + 1, answer))
def validation(y, x, num):
    # 가로줄 데이터 저장
    row = MAP[y]
    # 세로줄 데이터 저장
    col = []
    for i in range(9):
        col.append(MAP[i][x])
    # 사각형 데이터 저장
    dy, dx = y // 3, x // 3
    square = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            square[i][j] = MAP[dy * 3 + i][dx * 3 + j]
    # 가로 or 세로줄에 해당 숫자가 있는지 검사
    if (num in row) or (num in col):
        return False
    # 사각형에 해당 숫자가 있는지 검사사
    for i in range(3):
        if num in square[i]:
            return False
    return True


# MAP: 스도쿠판 정보
# input: 입력 정보
TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(9)]
    data = []
    for i in range(N):
        data.append(list(map(int, input().split())))

    answer = 0  # 게임 진행 횟수 저장 변수
    for i in range(N):
        y, x, num = data[i]
        if validation(y, x, num):  # 검증했을 때 가능하다면, MAP[y][x] 에 num 을 넣고 게임 횟수 증가
            MAP[y][x] = num
            answer += 1
        else: break  # 검증에 실패했다면, 반복문 탈출

    print('#{} {}'.format(tc + 1, answer))

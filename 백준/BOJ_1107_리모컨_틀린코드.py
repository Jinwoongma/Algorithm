# 남은 숫자들을 이용해서 만들 수 있는 가장 가까운 수로 이동한 뒤 + or -

# 누르는 번호의 자릿수가 목표 번호의 자릿수보다 적은 경우
def case1(r):
    global min_diff
    global push
    num = int(str(work[-1]) * r)
    diff = abs(num - goal)
    if diff < min_diff:
        min_diff = diff
        push = len(str(num)) + min_diff
    return

# 누르는 번호와 목표 번호가 자릿수가 같은 경우
def case2(index, n, r):
    global min_diff
    global push
    if index == r:  # 만들 수 있는 모든 경우의 수(중복 조합)를 구해서 비교한다
        num = int(''.join(map(str, arr)))
        diff = abs(num - goal)
        if diff < min_diff:
            min_diff = diff
            push = len(str(num)) + min_diff
        return
    for i in range(n):
        arr.append(work[i])
        case2(index + 1, n, r)
        arr.pop()


# 누르는 번호의 자릿수가 목표 번호의 자릿수보다 많은 경우
def case3(r):
    global min_diff
    global push
    if work[0] == 0:  # 누를 수 있는 번호에 0이 포함되어있으면 비교할 숫자의 첫번째 자리는 0이 되면 안됨
        num = int(str(work[1]) + str(0) * (r - 1))
    else:  # 0이 포함되어있지 않은 경우에서는 누를 수 있는 번호 중 가장 작은 숫자를 반복해서 누른다
        num = int(str(work[0]) * r)
    diff = abs(num - goal)
    if diff < min_diff:
        min_diff = diff
        push = len(str(num)) + min_diff
    return



goal = int(input())  # 목표 채널
goal_L = len(str(goal))  # 목표 채널의 자릿 수
trouble_num = int(input())  # 고장난 숫자의 개수
# 고장난 숫자가 0개면 입력받지 않고, 0개가 아닐 경우 입력받음.
if trouble_num != 0:
    trouble = list(map(int, input().split()))
else: trouble = []
# min_diff: 경우의 수로 나온 채널과 와 실제 목표 채널의 차이의 최솟값
# push: 차이가 최소일떄 버튼을 눌러야하는 횟수
min_diff, push = 0xffffffff, -1

# work: 동작하는 번호들의 리스트
work = []
for i in range(10):
    if i not in trouble:
        work.append(i)


# 동작하는 번호가 0개가 아닐 경우
if len(work) != 0:
    # case 1 (목표 채널의 자릿수가 1 이하일경우 case1은 돌릴 수가 없음)
    if goal_L > 1:
        case1(goal_L - 1)

    # case 2
    arr = []
    case2(0, len(work), goal_L)

    # case 3(동작하는 번호가 1개 이하일 경우 case3를 돌릴 수가 없음)
    if len(work) > 1:
        case3(goal_L + 1)

    # case1, case2, case3를 거친 뒤의 push 값을 목표 번호와 현재 번호(100)의 차이와 비교
    if push < abs(goal - 100):  # push 가 더 작을 경우 push 출력
        print(push)
    else:  # push 가 더 클 경우 차이 출력
        print(abs(goal - 100))
else:  # 동작하는 번호가 없으면 차이 출력
    print(abs(goal - 100))
from collections import deque


def is_possible(arr, N, board):
    y, x = arr
    if 0 <= y < N and 0 <= x < N and not board[y][x]:
        return True
    return False


def solution(board):
    answer = 0
    memo = set()
    N = len(board)
    dy = [-1, 1, 0, 0];
    dx = [0, 0, -1, 1]
    Q = deque()
    Q.append([[0, 0], [0, 1], 0])
    memo.add((0, 1))
    while Q:
        a, b, d = Q.popleft()
        print(a, b, d)
        if a == [N - 1, N - 1] or b == [N - 1, N - 1]:
            answer = d
            break
        for dir in range(6):
            if 0 <= dir < 4:
                ta = [a[0] + dy[dir], a[1] + dx[dir]]
                tb = [b[0] + dy[dir], b[1] + dx[dir]]
                if is_possible(ta, N, board) and is_possible(tb, N, board):
                    tidx = (ta[0] * N + ta[1], tb[0] * N + tb[1])
                    if tidx not in memo and tidx[::-1] not in memo:
                        memo.add(tidx)
                        Q.append([ta, tb, d + 1])
                        Q.append([tb, ta, d + 1])
            else:
                if dir == 4:  # a를 기준을 회전
                    if abs((ta[0] * N + ta[1]) - (tb[0] * N + tb[1])) == 1:  # 누워있을때
                        for dir2 in range(2):
                            if dir2 == 0:  # 위로 회전
                                if is_possible([b[0] - 1, b[1]], N, board) and is_possible([b[0] - 1, b[1] - 1], N,
                                                                                           board):
                                    ta, tb = a, [b[0] - 1, b[1] - 1]
                            elif dir2 == 1:  # 아래로 회전
                                if is_possible([b[0] + 1, b[1]], N, board) and is_possible([b[0] + 1, b[1] - 1], N,
                                                                                           board):
                                    ta, tb = a, [b[0] + 1, b[1] - 1]
                    else:  # 서있을 떄
                        for dir2 in range(2):
                            if dir2 == 0:  # 왼쪽 회전
                                if is_possible([b[0], b[1] - 1], N, board) and is_possible([b[0] + 1, b[1] - 1], N,
                                                                                           board):
                                    ta, tb = a, [b[0] + 1, b[1] - 1]
                            elif dir2 == 1:  # 오른쪽 회전
                                if is_possible([b[0], b[1] + 1], N, board) and is_possible([b[0] + 1, b[1] + 1], N,
                                                                                           board):
                                    ta, tb = a, [b[0] + 1, b[1] + 1]

                elif dir == 5:  # b를 기준을 회전
                    if abs((ta[0] * N + ta[1]) - (tb[0] * N + tb[1])) == 1:  # 누워있을 때 
                        for dir2 in range(2):
                            if dir2 == 0:  # 위로 회전
                                if is_possible([a[0] - 1, a[1]], N, board) and is_possible([a[0] - 1, a[1] + 1], N,
                                                                                           board):
                                    ta, tb = [a[0] - 1, a[1] + 1], b
                            elif dir2 == 1:  # 아래로 회전
                                if is_possible([a[0] + 1, a[1]], N, board) and is_possible([a[0] + 1, a[1] + 1], N,
                                                                                           board):
                                    ta, tb = [a[0] + 1, a[1] + 1], b
                    else:  # 서있을 때 
                        for dir2 in range(2):
                            if dir2 == 0:  # 왼쪽 회전
                                if is_possible([a[0], a[1] - 1], N, board) and is_possible([a[0] - 1, a[1] - 1], N,
                                                                                           board):
                                    ta, tb = [a[0] - 1, a[1] - 1], b
                            elif dir2 == 1:  # 오른쪽 회전
                                if is_possible([a[0], a[1] + 1], N, board) and is_possible([a[0] - 1, a[1] + 1], N,
                                                                                           board):
                                    ta, tb = [a[0] - 1, a[1] + 1], b

                if abs((ta[0] * N + ta[1]) - (tb[0] * N + tb[1])) == 1 or abs((ta[0] * N + ta[1]) - (tb[0] * N + tb[1])) == 5:
                    tidx = (ta[0] * N + ta[1], tb[0] * N + tb[1])
                    if tidx not in memo and tidx[::-1] not in memo:
                        memo.add(tidx)
                        Q.append([ta, tb, d + 1])
                        Q.append([tb, ta, d + 1])
    print(memo)

    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
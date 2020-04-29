# 23:13 ~ 23:46
from copy import deepcopy
from _collections import deque

def merge(dir):
    if dir == 0:
        for c in range(N):
            for r in range(N):
                index = r
                while True:
                    index += 1
                    if index == N: break
                    if MAP[index][c] != 0:
                        if MAP[index][c] == MAP[r][c]:
                            MAP[r][c], MAP[index][c] = MAP[r][c] * 2, 0
                            break
                        else: break
    elif dir == 1:
        for c in range(N):
            for r in range(N - 1, -1, -1):
                index = r
                while True:
                    index -= 1
                    if index < 0: break
                    if MAP[index][c] != 0:
                        if MAP[index][c] == MAP[r][c]:
                            MAP[r][c], MAP[index][c] = MAP[r][c] * 2, 0
                            break
                        else: break
    elif dir == 2:
        for r in range(N):
            for c in range(N):
                index = c
                while True:
                    index += 1
                    if index == N: break
                    if MAP[r][index] != 0:
                        if MAP[r][index] == MAP[r][c]:
                            MAP[r][c], MAP[r][index] = MAP[r][c] * 2, 0
                            break
                        else: break
    elif dir == 3:
        for r in range(N):
            for c in range(N - 1, -1, -1):
                index = c
                while True:
                    index -= 1
                    if index < 0: break
                    if MAP[r][index] != 0:
                        if MAP[r][index] == MAP[r][c]:
                            MAP[r][c], MAP[r][index] = MAP[r][c] * 2, 0
                            break
                        else: break


def move(dir):
    if dir == 0:
        for c in range(N):
            S = deque()
            for r in range(N):
                if MAP[r][c] != 0:
                    S.append(MAP[r][c])
                    MAP[r][c] = 0
            index = 0
            while S:
                MAP[index][c] = S.popleft()
                index += 1
    elif dir == 1:
        for c in range(N):
            S = deque()
            for r in range(N - 1, -1, -1):
                if MAP[r][c] != 0:
                    S.append(MAP[r][c])
                    MAP[r][c] = 0
            index = N - 1
            while S:
                MAP[index][c] = S.popleft()
                index -= 1
    elif dir == 2:
        for r in range(N):
            S = deque()
            for c in range(N):
                if MAP[r][c] != 0:
                    S.append(MAP[r][c])
                    MAP[r][c] = 0
            index = 0
            while S:
                MAP[r][index] = S.popleft()
                index += 1
    elif dir == 3:
        for r in range(N):
            S = deque()
            for c in range(N - 1, -1, -1):
                if MAP[r][c] != 0:
                    S.append(MAP[r][c])
                    MAP[r][c] = 0
            index = N - 1
            while S:
                MAP[r][index] = S.popleft()
                index -= 1


def solve(turn):
    global answer, MAP
    if turn == 5:
        sub_result = -1
        for r in range(N):
            sub_result = max(sub_result, max(MAP[r]))
        answer = max(answer, sub_result)
        return
    for i in range(4):  # 0: 상, 1: 하, 2: 좌, 3: 우
        prev = deepcopy(MAP)
        merge(i)
        move(i)
        solve(turn + 1)
        MAP = prev


N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
answer = -1
solve(0)
print(answer)
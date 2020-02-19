from copy import deepcopy
import sys
sys.stdin = open('input.txt', 'r')


def change(y, x, dir, map):
    ty, tx = y, x
    while True:
        ty += dy[dir]
        tx += dx[dir]
        if ty < 0 or ty >= N or tx < 0 or tx >= N: break
        if map[ty][tx] != 0:
            if map[ty][tx] == 1: continue
            else: break
        else:
            map[ty][tx] = 2


def isPossible(y, x, dir):
    ty, tx = y, x
    while True:
        ty += dy[dir]
        tx += dx[dir]
        if ty < 0 or ty >= N or tx < 0 or tx >= N: break
        if MAP[ty][tx] != 0: return False
    return True


def dfs(index, map):
    if index == L:
        for i in range(N):
            print(map[i])
        print()
        return
    for dir in range(4):
        if isPossible(core[index][0], core[index][1], dir):
            change(core[index][0], core[index][1], dir, map)
            dfs(index + 1, map)


TC = int(input())
for tc in range(TC):
    N = int(input())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    dy = [1, -1, 0, 0]; dx = [0, 0, -1, 1]

    core = []
    for i in range(N):
        for j in range(N):
            if MAP[i][j] == 1: core.append([i, j])

    L = len(core)

    new_MAP = deepcopy(MAP)
    dfs(0, new_MAP)
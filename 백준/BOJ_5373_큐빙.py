from copy import deepcopy
def turnLeft(arr):
    new_arr = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            new_arr[3 - j - 1][i] = arr[i][j]
    return new_arr


def turnRight(arr):
    new_arr = [[0 for _ in range(3)] for _ in range(3)]
    for i in range(3):
        for j in range(3):
            new_arr[j][3 - i - 1] = arr[i][j]
    return new_arr


def moveF(dir, center):
    if dir == '+': k = 1
    else: k = 3
    for i in range(k):
        temp = deepcopy(U)
        U[2][0], U[2][1], U[2][2] = L[2][2], L[1][2], L[0][2]
        L[0][2], L[1][2], L[2][2] = D[0][0], D[0][1], D[0][2]
        D[0][0], D[0][1], D[0][2] = R[2][0], R[1][0], R[0][0]
        R[2][0], R[1][0], R[0][0] = temp[2][2], temp[2][1], temp[2][0]


def moveB(dir):
    if dir == '+': k = 1
    else: k = 3
    for i in range(k):
        temp = deepcopy(U)
        U[0][0], U[0][1], U[0][2] = R[0][2], R[1][2], R[2][2]
        R[0][2], R[1][2], R[2][2] = D[2][2], D[2][1], D[2][0]
        D[2][2], D[2][1], D[2][0] = L[2][0], L[1][0], L[0][0]
        L[2][0], L[1][0], L[0][0] = temp[0][0], temp[0][1], temp[0][2]


def moveU(dir):
    if dir == '+': k = 1
    else: k = 3
    for i in range(k):
        F[0], R[0], B[0], L[0] = R[0], B[0], L[0], F[0]


def moveD(dir):
    if dir == '+': k = 1
    else: k = 3
    for i in range(k):
        F[2], R[2], B[2], L[2] = L[2], F[2], R[2], B[2]


def moveL(dir):
    if dir == '+': k = 1
    else: k = 3
    for i in range(k):
        temp = deepcopy(U)
        U[0][0], U[1][0], U[2][0] = B[2][2], B[1][2], B[0][2]
        B[2][2], B[1][2], B[0][2] = D[0][0], D[1][0], D[2][0]
        D[0][0], D[1][0], D[2][0] = F[0][0], F[1][0], F[2][0]
        F[0][0], F[1][0], F[2][0] = temp[0][0], temp[1][0], temp[2][0]


def moveR(dir):
    if dir == '+': k = 1
    else: k = 3
    for i in range(k):
        temp = deepcopy(U)
        U[0][2], U[1][2], U[2][2] = F[0][2], F[1][2], F[2][2]
        F[0][2], F[1][2], F[2][2] = D[0][2], D[1][2], D[2][2]
        D[0][2], D[1][2], D[2][2] = B[2][0], B[1][0], B[0][0]
        B[2][0], B[1][0], B[0][0] = temp[0][2], temp[1][2], temp[2][2]


TC = int(input())
for tc in range(TC):
    U = [['w', 'w', 'w'], ['w', 'w', 'w'], ['w', 'w', 'w']]
    D = [['y', 'y', 'y'], ['y', 'y', 'y'], ['y', 'y', 'y']]
    F = [['r', 'r', 'r'], ['r', 'r', 'r'], ['r', 'r', 'r']]
    B = [['o', 'o', 'o'], ['o', 'o', 'o'], ['o', 'o', 'o']]
    L = [['g', 'g', 'g'], ['g', 'g', 'g'], ['g', 'g', 'g']]
    R = [['b', 'b', 'b'], ['b', 'b', 'b'], ['b', 'b', 'b']]

    N = int(input())
    move = list(map(str, input().split()))
    for i in range(N):
        face, dir = move[i][0], move[i][1]
        if face == 'F':
            moveF(dir, F)
            if dir == '+': F = turnRight(F)
            else: F = turnLeft(F)
        elif face == 'B':
            moveB(dir)
            if dir == '+': B = turnRight(B)
            else: B = turnLeft(B)
        elif face == 'U':
            moveU(dir)
            if dir == '+': U = turnRight(U)
            else: U = turnLeft(U)
        elif face == 'D':
            moveD(dir)
            if dir == '+': D = turnRight(D)
            else: D = turnLeft(D)
        elif face == 'L':
            moveL(dir)
            if dir == '+': L = turnRight(L)
            else: L = turnLeft(L)
        elif face == 'R':
            moveR(dir)
            if dir == '+': R = turnRight(R)
            else: R = turnLeft(R)

    for i in range(3):
        print(''.join(U[i]))
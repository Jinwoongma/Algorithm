def play():
    for i in range(10):
        for j in range(10):
            if board[i][j] == '.':
                if check(i, j):
                    return 1
    return 0

def check(i, j):
    if go(i, j, [0, 1]): return True
    if go(i, j, [2, 3]): return True
    if go(i, j, [4, 5]): return True
    if go(i, j, [6, 7]): return True
    return False

def go(i, j, dir):
    t_cnt = 1
    for d in dir:
        cnt = 0
        ni, nj = i+di[d], j+dj[d]
        for _ in range(5):
            if not(0 <= ni < 10 and 0 <= nj <10):
                t_cnt += cnt
                break
            if board[ni][nj] == 'X':
                cnt += 1
                ni, nj = ni+di[d], nj+dj[d]
            else:
                t_cnt += cnt
                break
    return True if t_cnt >= 5 else False

board = [list(input()) for _ in range(10)]
di = [-1, 1, 0, 0, -1, 1, -1, 1]
dj = [0, 0, -1, 1, -1, 1, 1, -1]
print(play())
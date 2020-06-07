from _collections import deque
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]

def solution(board):
    answer = 0xffffff
    N = len(board)
    D = [[0xffffff for _ in range(N)] for _ in range(N)]
    D[0][0] = 0
    for i in range(4):
        q = deque()
        q.append([0, 0, i, D])
        while q:
            y, x, before_dir, cur = q.popleft()
            # print(y, x, before_dir)
            for dir in range(4):
                ty, tx = y + dy[dir], x + dx[dir]
                if ty < 0 or ty >= N or tx < 0 or tx >= N: continue
                if dir == before_dir:
                    cost = 100
                else:
                    cost = 600
                if board[ty][tx] == 0 and cur[ty][tx] >= cur[y][x] + cost:
                    cur[ty][tx] = cur[y][x] + cost
                    q.append([ty, tx, dir, cur])
        # for i in range(N):
        #     print(D[i])
        # print()
        answer = min(answer, D[N - 1][N - 1])
    return answer

print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
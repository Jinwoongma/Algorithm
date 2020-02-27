r, c = map(int, input().split())
MAP = [list(map(int, input().split())) for _ in range(r)]
MAX = -1
tetris1 = [[[0, 0], [0, 1], [0, 2], [0, 3]],
          [[0, 0], [1, 0], [2, 0], [3, 0]]]
tetris2 = [[[0, 0], [0, 1], [1, 0], [1, 1]]]
tetris3 = [[[0, 0], [1, 0], [2, 0], [2, 1]],
           [[0, 0], [0, 1], [0, 2], [-1, 2]],
           [[0, 0], [-1, 0], [-2, 0], [-2, -1]],
           [[0, 0], [0, -1], [0, -2], [1, -2]],
           [[0, 0], [1, 0], [2, 0], [2, -1]],
           [[0, 0], [0, 1], [0, 2], [1, 2]],
           [[0, 0], [-1, 0], [-2, 0], [-2, 1]],
           [[0, 0], [0, -1], [0, -2], [-1, -2]]
           ]
tetris4 = [[[0, 0], [1, 0], [1, 1], [2, 1]],
           [[0, 0], [0, 1], [-1, 1], [-1, 2]],
           [[0, 0], [1, 0], [1, -1], [2, -1]],
           [[0, 0], [0, 1], [1, 1], [1, 2]]]
tetris5 = [[[0, 0], [0, 1], [0, 2], [1, 1]],
           [[0, 0], [-1, 0], [-2, 0], [-1, 1]],
           [[0, 0], [0, -1], [0, -2], [-1, -1]],
           [[0, 0], [1, 0], [2, 0], [1, -1]]]

for i in range(r):
    for j in range(c):
        y, x = i, j
        # 모양 1
        for s in range(2):
            SUM = 0
            for k in range(4):
                ty = y + tetris1[s][k][0]
                tx = x + tetris1[s][k][1]
                if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
                SUM += MAP[ty][tx]
            MAX = max(MAX, SUM)

        # 모양 2
        for s in range(1):
            SUM = 0
            for k in range(4):
                ty = y + tetris2[s][k][0]
                tx = x + tetris2[s][k][1]
                if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
                SUM += MAP[ty][tx]
            MAX = max(MAX, SUM)

        # 모양 3
        for s in range(8):
            SUM = 0
            for k in range(4):
                ty = y + tetris3[s][k][0]
                tx = x + tetris3[s][k][1]
                if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
                SUM += MAP[ty][tx]
            MAX = max(MAX, SUM)

        # 모양 4
        for s in range(4):
            SUM = 0
            for k in range(4):
                ty = y + tetris4[s][k][0]
                tx = x + tetris4[s][k][1]
                if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
                SUM += MAP[ty][tx]
            MAX = max(MAX, SUM)

        # 모양 5
        for s in range(4):
            SUM = 0
            for k in range(4):
                ty = y + tetris5[s][k][0]
                tx = x + tetris5[s][k][1]
                if ty < 0 or ty >= r or tx < 0 or tx >= c: continue
                SUM += MAP[ty][tx]
            MAX = max(MAX, SUM)

print(MAX)



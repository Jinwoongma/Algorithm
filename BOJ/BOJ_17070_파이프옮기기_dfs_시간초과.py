def move(pipe, shape):
    global count
    if pipe[1][0] == N - 1 and pipe[1][1] == N - 1:
        count += 1
        return

    if shape == 0:  # 가로 모양
        if pipe[1][1] + 1 < N and MAP[pipe[1][0]][pipe[1][1] + 1] == 0:
            new_pipe = [pipe[1], [pipe[1][0], pipe[1][1] + 1]]
            move(new_pipe, 0)  # 가로 모양 그대로

        if pipe[1][1] + 1 < N and pipe[1][0] + 1 < N and MAP[pipe[1][0] + 1][pipe[1][1]] == 0 and MAP[pipe[1][0]][pipe[1][1] + 1] == 0 and MAP[pipe[1][0] + 1][pipe[1][1] + 1] == 0:
            new_pipe = [pipe[1], [pipe[1][0] + 1, pipe[1][1] + 1]]
            move(new_pipe, 2)  # 대각선 모양으로

    elif shape == 1:  # 세로 모양
        if pipe[1][0] + 1 < N and MAP[pipe[1][0] + 1][pipe[1][1]] == 0:
            new_pipe = [pipe[1], [pipe[1][0] + 1, pipe[1][1]]]
            move(new_pipe, 1)  # 세로 모양 그대로

        if pipe[1][1] + 1 < N and pipe[1][0] + 1 < N and MAP[pipe[1][0] + 1][pipe[1][1]] == 0 and MAP[pipe[1][0]][pipe[1][1] + 1] == 0 and MAP[pipe[1][0] + 1][pipe[1][1] + 1] == 0:
            new_pipe = [pipe[1], [pipe[1][0] + 1, pipe[1][1] + 1]]
            move(new_pipe, 2)  # 대각선 모양으로

    elif shape == 2:  # 대각선 모양
        if pipe[1][1] + 1 < N and MAP[pipe[1][0]][pipe[1][1] + 1] == 0:
            new_pipe = [pipe[1], [pipe[1][0], pipe[1][1] + 1]]
            move(new_pipe, 0)  # 가로 모양으로

        if pipe[1][0] + 1 < N and MAP[pipe[1][0] + 1][pipe[1][1]] == 0:
            new_pipe = [pipe[1], [pipe[1][0] + 1, pipe[1][1]]]
            move(new_pipe, 1)  # 세로 모양으로

        if pipe[1][1] + 1 < N and pipe[1][0] + 1 < N and MAP[pipe[1][0] + 1][pipe[1][1]] == 0 and MAP[pipe[1][0]][
            pipe[1][1] + 1] == 0 and MAP[pipe[1][0] + 1][pipe[1][1] + 1] == 0:
            new_pipe = [pipe[1], [pipe[1][0] + 1, pipe[1][1] + 1]]
            move(new_pipe, 2)  # 대각선 모양으로

N = int(input())
MAP = [list(map(int, input().split())) for _ in range(N)]
dy = [-1, 1, 0, 0]; dx = [0, 0, -1, 1]
pipe = [[0, 0], [0, 1]]
count = -1
move(pipe, 0)
print(count)
king, stone, N = map(str, input().split())
king_x, king_y, stone_x, stone_y = king[0], king[1], stone[0], stone[1]
N, king_x, stone_x = int(N), int(ord(king_x) - ord('A')), int(ord(stone_x) - ord('A'))
king_y, stone_y = 8 - int(king_y), 8 - int(stone_y)
D = {'R': 0, 'L': 1, 'B': 2, 'T': 3, 'RT': 4, 'LT': 5, 'RB': 6, 'LB': 7}
dy = [0, 0, 1, -1, -1, -1, 1, 1]
dx = [1, -1, 0, 0, 1, -1, 1, -1]

for i in range(N):
    d = D[str(input())]
    nking_y, nking_x = king_y + dy[d], king_x + dx[d]
    if nking_y < 0 or nking_y >= 8 or nking_x < 0 or nking_x >= 8: continue
    if nking_y == stone_y and nking_x == stone_x:
        nstone_y, nstone_x = stone_y + dy[d], stone_x + dx[d]
        if nstone_y < 0 or nstone_y >= 8 or nstone_x < 0 or nstone_x >= 8: continue
    else: nstone_y, nstone_x = stone_y, stone_x
    king_y, king_x, stone_y, stone_x = nking_y, nking_x, nstone_y, nstone_x

king_y, stone_y = str(8 - king_y), str(8 - stone_y)
king_x, stone_x = chr(ord('A') + king_x), chr(ord('A') + stone_x)

print(king_x + king_y)
print(stone_x + stone_y)
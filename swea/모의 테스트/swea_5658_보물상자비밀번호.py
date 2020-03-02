import sys
sys.stdin = open('input.txt', 'r')
TC = int(input())
for tc in range(TC):
    N, K = map(int, input().split())
    num = str(input())
    div = N // 4

    bin_arr = []
    for i in range(div):
        hex_arr = []

        for j in range(4):
            hex_arr.append(num[div * j:div * j + div])

        for j in range(len(hex_arr)):
            bin_arr.append(int(hex_arr[j], 16))

        num = num[-1] + num[:-1]

    new_arr = sorted(list(set(bin_arr)), reverse=True)

    print('#{} {}'.format(tc + 1, new_arr[K - 1]))
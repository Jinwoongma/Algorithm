import sys
sys.stdin = open("input_1216.txt", "r")

def get_transport(arr):
    new_arr = [[0 for r in range(100)] for c in range(100)]
    result = []
    for i in range(100):
        for j in range(100):
            new_arr[i][j] = arr[j][i]
        temp = ''.join(new_arr[i])
        result.append(temp)
    return result

def get_reverse(input_str):
    new_str = ''
    L = len(input_str)
    for i in range(L):
        new_str += input_str[-1-i]
    return new_str

for tc in range(1, 11):
    t = int(input())
    data = []
    for i in range(100):
        data.append(input())

    max_length = 0
    for i in range(100):
        for j in range(100):
            for k in range(1, 101):
                temp_str = data[i][j:j+k]
                if temp_str == get_reverse(temp_str):
                    if len(temp_str) >= max_length:
                        max_length = len(temp_str)

    transport_data = get_transport(data)
    for i in range(100):
        for j in range(100):
            for k in range(1, 101):
                temp_str = transport_data[i][j:j+k]
                if temp_str == get_reverse(temp_str):
                    if len(temp_str) >= max_length:
                        max_length = len(temp_str)

    print('#{} {}'.format(tc, max_length))
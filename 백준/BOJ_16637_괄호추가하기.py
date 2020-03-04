def calc(n1, sign, n2):
    if sign == '+':
        return str(int(n1) + int(n2))
    elif sign == '-':
        return str(int(n1) - int(n2))
    elif sign == '*':
        return str(int(n1) * int(n2))


def check(arr):
    for j in range(len(arr) - 1):
        if abs(arr[j] - arr[j + 1]) == 1:
            return False
    return True


def subset(n):
    global max_result
    for i in range(1 << n):
        arr = []
        for j in range(n):
            if i & (1 << j):
                arr.append(temp[j])

        new_data = data[:]
        if check(arr):
            if len(arr) == 0:
                new_data = data[:]
            else:
                ind = 0
                cnt = -1
                new_data = data[:]
                length = N
                while True:
                    if ind == length:
                        break
                    if data[ind] not in '*+-':
                        cnt += 1
                        if cnt in arr:
                            result = calc(new_data[ind], new_data[ind + 1], new_data[ind + 2])
                            new_data = new_data[:ind] + [result] + new_data[ind + 3:]
                            length -= 2
                            continue
                    ind += 1

        result = int(new_data[0])
        for j in range(len(new_data)):
            if new_data[j] in '*+-':
                result = calc(result, new_data[j], new_data[j + 1])
        max_result = max(max_result, int(result))

N = int(input())
data = list(map(str, input().strip()))
change = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
temp = list(range(N // 2))
max_result = -1 * (2 ** 31)
subset(N//2)
print(max_result)
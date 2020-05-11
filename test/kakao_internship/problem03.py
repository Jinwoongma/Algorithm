from _collections import deque

def counting_sort(array, max):
    counting_array = [0] * (max + 1)
    for i in array:
        counting_array[i] += 1
    for i in range(max):
        counting_array[i + 1] += counting_array[i]
    output_array = [-1] * len(array)

    for i in array:
        output_array[counting_array[i] - 1] = i
        counting_array[i] -= 1
    return output_array

def solve(data, L):
    min_range = []
    while True:
        min_length = min([len(x) for x in data])
        if min_length <= 0: break
        before_t = [x[0] for x in data]
        t = counting_sort(before_t, L)
        a, b, i = t[-1], t[0], before_t.index(t[0])  # 최대, 최소, 인덱스
        diff = a - b
        if min_range:
            if (min_range[0] - min_range[1]) > diff:  # 차이의 최솟값 갱신
                min_range = [a, b]
        else:
            min_range = [a, b]
        data[i].popleft()

    return min_range[::-1]


def solution(gems):
    D = {}
    index = 0
    for g in gems:
        if g not in D:
            D[g] = index
            index += 1
    arr = [deque() for _ in range(len(D))]
    for i in range(len(gems)):
        arr[D[gems[i]]].append(i + 1)

    return list(solve(arr, len(gems)))

print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
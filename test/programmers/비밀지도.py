def decode(num, n):
    bin = [0] * n
    index = n - 1
    while num > 0:
        num, r = num // 2, num % 2
        bin[index] = r
        index -= 1
    return bin

def solution(n, arr1, arr2):
    answer = [[' ' for _ in range(n)] for _ in range(n)]
    print(answer)
    for i in range(n):
        bin1 = decode(arr1[i], n)
        bin2 = decode(arr2[i], n)
        print(bin1, bin2)
        for j in range(n):
            if bin1[j] or bin2[j]:
                answer[i][j] = '#'
        answer[i] = ''.join(answer[i])
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30,  1, 21, 17, 28]))
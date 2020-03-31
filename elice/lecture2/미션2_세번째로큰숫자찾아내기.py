def thirdMax(nums):
    INF = float('inf')
    memory = [-INF] * 3

    # 실제 검색 연산
    for n in nums:
        if n <= memory[-1]:
            continue

        for i, m in enumerate(memory):
            if (i == 0 and n > m) or m < n < memory[i-1]:
                for j in range(len(memory)-2, i-1, -1):
                    memory[j+1] = memory[j]
                memory[i] = n
                break

    return memory[-1]

def main():
    print(thirdMax([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23])) # should return 34

if __name__ == "__main__":
    main()

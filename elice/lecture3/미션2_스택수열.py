def isStackSequence(nums):
    S = []
    count = 1
    for num in nums:
        while count <= num:  # count와 num이 같은수를 찾는다.
            S.append(count)  # 그전까진 1부터 count까지 num_list에 저장한다.
            count += 1
        if S[-1] == num:
            S.pop()  # num과 num_list의 마지막 값이 같다면 pop해준다.
        else:
            return False
    return True


def main():
    print(isStackSequence([2, 1, 4, 3]))  # True가 리턴되어야 합니다
    print(isStackSequence([3, 1, 2, 4]))  # False가 리턴되어야 합니다


if __name__ == "__main__":
    main()
def findDifference(str1, str2):
    dict1, dict2 = {}, {}
    for c in str1:
        if c in dict1:
            dict1[c] += 1
        else:
            dict1[c] = 1

    for c in str2:
        if c in dict2:
            dict2[c] += 1
        else:
            dict2[c] = 1

    for key2, value2 in dict2.items():
        if key2 not in dict1.keys():
            return key2
        if value2 > dict1[key2]:
            return key2


def main():
    print(findDifference("apple", "aalppe"))


if __name__ == "__main__":
    main()

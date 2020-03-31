def isAnagram(str1, str2):
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

    for key1, value1 in dict1.items():
        if key1 not in dict2.keys():
            return False
        if value1 != dict2[key1]:
            return False
    return True


def main():
    print(isAnagram('iamlordvoldemort', 'tommarvoloriddle'))  # should return True
    print(isAnagram('cat', 'cap'))  # should return False


if __name__ == "__main__":
    main()

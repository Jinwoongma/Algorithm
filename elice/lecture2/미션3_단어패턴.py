def wordPattern(pattern, strList):
    P = {}
    for i in range(len(pattern)):
        if pattern[i] in P:
            if strList[i] != P[pattern[i]]:
                return False
        else:
            if strList[i] in P.values():
                return False
            else:
                P[pattern[i]] = strList[i]
    return True


def main():
    print(wordPattern("aabb", ["elice", "elice", "alice", "alice"]))  # should return True
    print(wordPattern("abab", ["elice", "elice", "alice", "alice"]))  # should return False


if __name__ == "__main__":
    main()

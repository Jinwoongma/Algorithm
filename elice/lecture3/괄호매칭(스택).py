def isParenthesisValid(st):
    S = []
    for c in st:
        if c in '({<[':
            S.append(c)
        else:
            if len(S) == 0:
                return False
            temp = S.pop()
            if c == ')' and temp != '(':
                return False
            elif c == '}' and temp != '{':
                return False
            elif c == '>' and temp != '<':
                return False
            elif c == ']' and temp != '[':
                return False
    if len(S) > 0:
        return False
    return True


def main():
    examples = ["({()})", "[]<>{}", ")(" "<]", "<(>)"]
    for example in examples:
        print(example, isParenthesisValid(example))


if __name__ == "__main__":
    main()
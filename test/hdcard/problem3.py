def solution(registered_list, new_id):
    answer = ''
    R = set(registered_list)
    if new_id not in R:
        return new_id
    else:
        s, n = '', ''
        for i in range(len(new_id)):
            if ord('a') <= ord(new_id[i]) <= ord('z'):
                s += new_id[i]
            elif ord('0') <= ord(new_id[i]) <= ord('9'):
                n += new_id[i]

        if n == '': n = 0
        else: n = int(n)

        while new_id in R:
            n += 1
            new_id = s + str(n)
    return new_id


a = [["apple1", "orange", "banana3"], 'apple']


print(solution(a[0], a[1]))
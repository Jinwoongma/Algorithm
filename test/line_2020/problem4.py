def solution(snapshots, transactions):
    data = {}
    answer = []
    checkID = [False] * 100010
    for key, val in snapshots:
        data[key] = int(val)

    for ID, TYPE, name, amount in transactions:
        if checkID[int(ID)]: continue
        checkID[int(ID)] = True
        if TYPE == 'SAVE':
            if name in data:
                data[name] += int(amount)
            else:
                data[name] = int(amount)
        else:
            data[name] -= int(amount)

    for key, value in data.items():
        answer.append([str(key), str(value)])

    return answer

snapshots = [
    ["ACCOUNT1", "100"],
    ["ACCOUNT2", "150"],
]

transactions = [
    ["1", "SAVE", "ACCOUNT2", "100"],
    ["2", "WITHDRAW", "ACCOUNT1", "50"],
    ["1", "SAVE", "ACCOUNT2", "100"],
    ["4", "SAVE", "ACCOUNT3", "500"],
    ["3", "WITHDRAW", "ACCOUNT2", "30"]
]

print(solution(snapshots, transactions))
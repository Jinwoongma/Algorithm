

def solution(purchase):
    calendar = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    check = [0] * 366

    for p in purchase:
        date, money = p.split(' ')
        year, month, day = map(int, date.split('/'))
        start = 0
        for i in range(1, month):
            start += calendar[i]
        start += day
        for j in range(start, start + 30):
            check[j] += int(money)

        tier = [0] * 5
        for i in range(1, 366):
            if 0 <= check[i] < 10000: tier[0] += 1
            elif 10000 <= check[i] < 20000: tier[1] += 1
            elif 20000 <= check[i] < 50000: tier[2] += 1
            elif 50000 <= check[i] < 100000: tier[3] += 1
            else: tier[4] += 1

    return tier


a = [["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"],
     ["2019/01/30 5000", "2019/04/05 10000", "2019/06/10 20000", "2019/08/15 50000", "2019/12/01 100000"]
     ]

for i in a:
    print(solution(i))
def babygin(player):
    for i in range(10):
        if player[i] == 3:
            return True
        if i + 3 <= 10 and player[i] and player[i + 1] and player[i + 2]:
            return True

TC = int(input())
for tc in range(TC):
    cards = list(map(int, input().split()))
    player1 = [0] * 10
    player2 = [0] * 10
    winner = 0
    for i in range(12):
        if i % 2 == 1:
            player2[cards[i]] += 1
            if i > 5:
                if babygin(player2):
                    winner = 2
                    break
        else:
            player1[cards[i]] += 1
            if i > 5:
                if babygin(player1):
                    winner = 1
                    break
    print('#{} {}'.format(tc + 1, winner))
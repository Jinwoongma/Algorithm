cor = {1:0, 2:1, 3:2, 4:3, 5:4, 6:5, 7:6, 8:7, 9:8, 0:10}

def solution(numbers, hand):
    answer = ''
    l, r = 9, 11
    l_y, l_x = l // 3, l % 3
    r_y, r_x = r // 3, r % 3
    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            l_y, l_x = cor[num] // 3, cor[num] % 3
        elif num in [3, 6, 9]:
            answer += 'R'
            r_y, r_x = cor[num] // 3, cor[num] % 3
        elif num in [2, 5, 8, 0]:
            l_diff = abs(cor[num] // 3 - l_y) + abs(cor[num] % 3 - l_x)
            r_diff = abs(cor[num] // 3 - r_y) + abs(cor[num] % 3 - r_x)
            if l_diff < r_diff:
                answer += 'L'
                l_y, l_x = cor[num] // 3, cor[num] % 3
            elif l_diff > r_diff:
                answer += 'R'
                r_y, r_x = cor[num] // 3, cor[num] % 3
            elif l_diff == r_diff:
                if hand == 'left':
                    answer += 'L'
                    l_y, l_x = cor[num] // 3, cor[num] % 3
                else:
                    answer += 'R'
                    r_y, r_x = cor[num] // 3, cor[num] % 3
    return answer


a = [
    [[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"],
    [[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	"left"],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"]
]

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],	"left"))
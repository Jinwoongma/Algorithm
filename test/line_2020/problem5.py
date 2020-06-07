def solution(dataSource, tags):
    answer = []
    data = []
    for s in dataSource:
        data.append([s[0], set(s[1:])])

    score = [[0, data[i][0]] for i in range(len(data))]
    for i in range(len(data)):
        for t in tags:
            if t in data[i][1]:
                score[i][0] += 1

    score = sorted(score, key=lambda x: (-x[0], x[1]))
    i = 0
    while True:
        if i >= len(score) or len(answer) == 10:
            break
        if score[i][0] > 0:
            answer.append(score[i][1])
        i += 1
    return answer

dataSource = [
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"],
    ["doc6", "t1", "t2", "t4"],
    ["doc7", "t1", "t2", "t4"],
    ["doc8", "t1", "t2", "t4"],
    ["doc9", "t1", "t2", "t4"],
    ["doc10", "t1", "t2", "t4"],
    ["doc11", "t1", "t2", "t4"],
    ["doc12", "t1", "t2", "t4"],
    ["doc13", "t1", "t2", "t4"],

]

tags = ["t1", "t2", "t3"]

print(solution(dataSource, tags))
class Node:
    def __init__(self, data, link):
        self.data = data
        self.link = link

def addtoFirst(data):
    global Head
    Head = Node(data, Head)


def add(pre, data):
    pre.link = Node(data, pre.link)


def addtoLast(data):
    global Head
    if Head == None:
        Head = Node(data, None)
    else:
        p = Head
        while p.link != None:
            p = p.link
        p.link = Node(data, None)

TC = int(input())

for tc in range(TC):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    Head = None
    for i in range(len(arr)):
        addtoLast(arr[i])
    add_arr = [list(map(int, input().split())) for _ in range(M - 1)]
    length = 0
    for add_list in add_arr:
        node = Head
        length += len(add_list)
        for j in range(length):
            if node.data > add_list[0]:
                if j == 0:
                    for i in range(len(add_list) - 1, -1, -1):
                        addtoFirst(add_list[i])
                    break
                elif j == 1:
                    for i in range(len(add_list) - 1, -1, -1):
                        add(Head, add_list[i])
                    break
                else:
                    for i in range(len(add_list) - 1, -1, -1):
                        add(prev_node, add_list[i])
                    break
            if not j:
                node = Head.link
            else:
                node = node.link
                if j > 1:
                    prev_node = prev_node.link
                else:
                    prev_node = Head.link
        else:
            for i in range(len(add_list) - 1, -1, -1):
                add(prev_node, add_list[i])

    result = []
    count = 0
    while Head.link != None:
        count += 1
        if (length + N) - count <= 9:
            result.insert(0, str(Head.data))
        Head = Head.link
    result.insert(0, str(Head.data))
    print('#{} {}'.format(tc + 1, ' '.join(result)))
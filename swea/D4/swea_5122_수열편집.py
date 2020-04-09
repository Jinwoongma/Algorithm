class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        newNode = Node('HEAD')
        self.head = newNode
        self.tail = newNode
        self.before = None
        self.current = None

    def append(self, data):
        newNode = Node(data)
        self.tail.next = newNode
        self.tail = newNode

    def move_to(self, D):
        self.current = self.head.next
        self.before = self.head
        for _ in range(D):
            if self.current is None:
                return False
            self.before = self.current
            self.current = self.current.next
        return True

    def insert(self, idx, data):
        newNode = Node(data)
        self.move_to(idx)
        self.before.next = newNode
        newNode.next = self.current

    def delete(self, idx):
        self.move_to(idx)
        self.before.next = self.current.next

    def change(self, idx, data):
        self.move_to(idx)
        self.current.data = data

    def print_result(self, idx):
        if self.move_to(idx):
            return self.current.data
        else:
            return -1

TC = int(input())
for tc in range(TC):
    N, M, L = map(int, input().split())
    llst = LinkedList()
    for i in map(int, input().split()):
        llst.append(i)
    for _ in range(M):
        data = list(input().split())
        if data[0] == 'I':
            llst.insert(int(data[1]), int(data[2]))
        elif data[0] == 'D':
            llst.delete(int(data[1]))
        elif data[0] == 'C':
            llst.change(int(data[1]), int(data[2]))

    print('#{} {}'.format(tc + 1, llst.print_result(L)))

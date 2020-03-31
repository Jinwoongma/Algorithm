# 연결 리스트의 노드. 단일 연결 리스트의 경우입니다.
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


# 연결 리스트 클래스. head 와 tail을 가지고 있으며, 가장 뒤에 새로운 노드를 추가하는 addToEnd 함수가 있습니다.
class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head

    def addToEnd(self, node):
        self.tail.next = node
        self.tail = node

    def __str__(self):
        node = self.head
        toPrint = []
        while node:
            toPrint.append(str(node.val))
            node = node.next
        return "->".join(toPrint)


####################################################################################################################################

# 주어진 연결 리스트 ll을 배열로 변환해 봅시다.
# 이때 연결 리스트 LinkedList의 객체가 입력으로 주어진다고 가정합니다.
def toArray(llNode):
    ret = []
    temp = ''
    node = llNode.head
    while node:
        ret.append(int(node.val))
        node = node.next
    return ret


# 주어진 배열을 연결 리스트로 변환 해 봅시다.
def toLinkedList(lst):
    L = LinkedList(Node(lst[0]))
    for i in range(1, len(lst)):
        L.addToEnd(Node(lst[i]))
    return L


def example():
    ## Linkedlist 클래스와 Node 클래스를 사용하는 예시입니다.
    ll = LinkedList(Node(3))
    ll.addToEnd(Node(4))
    ll.addToEnd(Node(8))
    print(ll)
    print(ll.head)
    print(ll.tail)


def main():
    example()
    nums = [2, 8, 19, 37, 4, 5]
    ll = toLinkedList(nums)
    print(ll)
    lst = toArray(ll)
    print(lst)


if __name__ == "__main__":
    main()

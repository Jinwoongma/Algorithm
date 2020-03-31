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


# 주어진 배열을 linkedlist로 변환해서 돌려줍니다. 실습 3-1을 참조하세요
def toLinkedList(lst):
    ll = LinkedList(Node(lst[0]))
    for i in range(1, len(lst)):
        ll.addToEnd(Node(lst[i]))

    return ll


####################################################################################################################################

def deleteNode(ll, valToDelete):
    idx = 0
    curn = ll.head
    prevn = None
    nextn = ll.head.next

    while curn:
        if curn.val == valToDelete:
            if idx == 0:
                ll.head = nextn
                break
            else:
                prevn.next = nextn
                break
        else:
            if curn.next:
                prevn = curn
                curn = nextn
                nextn = nextn.next
            else:
                break
        idx += 1


def main():
    nums = [2, 8, 19, 37, 4, 5]
    ll = toLinkedList(nums)
    print(ll)
    deleteNode(ll, 2)
    print(ll)
    deleteNode(ll, 5)
    print(ll)
    deleteNode(ll, 8)
    print(ll)
    deleteNode(ll, 4)
    print(ll)
    deleteNode(ll, 5)
    print(ll)
    deleteNode(ll, 37)
    print(ll)


if __name__ == "__main__":
    main()
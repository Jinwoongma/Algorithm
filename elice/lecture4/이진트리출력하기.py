from collections import deque

# ====이 문제를 풀기 위해 필요한 클래스와 함수들입니다. 따로 수정 할 필요는 없습니다.
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def listToCompleteBinaryTree(lst):
    def helper(index):
        if index >= len(lst):
            return None
        node = Node(lst[index])
        node.left = helper(index * 2 + 1)
        node.right = helper(index * 2 + 2)
        return node

    return helper(0)


# =================================================================================
def printTree(node):
    all_lines = []
    line = []
    Q = deque()
    Q.append(node)
    Q.append(Node(-1))
    while Q:
        node = Q.popleft()
        if not node:
            continue
        else:
            if node.val == -1:
                if len(Q) > 0:
                    all_lines.append(line)
                    line = []
                    Q.append(Node(-1))
            else:
                line.append(node.val)
                Q.append(node.left)
                Q.append(node.right)

    return all_lines


def main():
    node = listToCompleteBinaryTree([1, 2, 3, 4, 5, 6, 7])
    print(printTree(node))  # [[1], [2, 3], [4, 5, 6, 7]]


if __name__ == "__main__":
    main()

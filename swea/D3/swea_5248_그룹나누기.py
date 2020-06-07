# # 1. 반복문 disjoint-set
# TC = int(input())
# for tc in range(TC):
#     N, M = map(int, input().split())
#     nums = list(map(int, input().split()))
#     root = [i for i in range(1, N + 1)]
#     for i in range(M):
#         a, b = nums[i * 2], nums[i * 2 + 1]
#         target = root[b - 1]
#         for j in range(len(root)):
#             if root[j] == target:
#                 root[j] = root[a - 1]
#     print('#{} {}'.format(tc + 1, len(set(root))))


# 2. 트리구조 disjoint-set
class DisjointSet:
    def __init__(self, n):
        self.data = [-1 for _ in range(n)]  # -1은 root node를 의미
        self.size = n  # 트리(root node)의 개수

    def find(self, index):
        value = self.data[index]
        if value < 0:
            return index
        return self.find(value)

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)

        if x_root == y_root:
            return

        if self.data[x_root] < self.data[y_root]:  # 원소의 수가 더 많은 트리를 찾는다(리스트 값이 더 낮은)
            self.data[x_root] += self.data[y_root]  # 원소의 수가 더 적은 트리를 많은 트리에 합한다.
            self.data[y_root] = x_root
        else:
            self.data[y_root] += self.data[x_root]
            self.data[x_root] = y_root

        self.size -= 1  # 트리의 수를 하나 뺀다.

TC = int(input())
for tc in range(TC):
    N, M = map(int, input().split())
    nums = list(map(int, input().split()))
    disjoint_set = DisjointSet(N)
    for i in range(M):
        disjoint_set.union(nums[i * 2] - 1, nums[i * 2 + 1] - 1)
        print(disjoint_set.data)
    print('#{} {}'.format(tc + 1, disjoint_set.size))

import sys
sys.setrecursionlimit(10**8)

class UnionFind:
    def __init__(self):
        self.data = dict()

    def find(self, num):
        if num not in self.data:
            return num
        return self.find(self.data[num])

    def union(self, num):
        parent = self.find(num)

        while parent in self.data:
            parent = self.data[parent]

        self.data[parent] = parent + 1

def solution(k, room_number):
    answer = []

    u = UnionFind()
    for n in room_number:
        parent = u.find(n)
        answer.append(parent)
        u.union(n)

    return answer
import sys
input = sys.stdin.readline

class DisjointSet():
    def __init__(self, n):
        self.size = n
        self.data = list(range(n))
        self.rank = [0] * n

    def find(self, index):
        while index != self.data[index]:
            index = self.data[index]
        return index

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        if x == y:
            return
        if self.rank[x] < self.rank[y]:
            self.data[x] = y
            self.rank[y] += 1
        else:
            self.data[y] = x
            self.rank[x] += 1


N, M = map(int, input().split())
S = DisjointSet(N + 1)
for i in range(M):
    s, a, b = map(int, input().split())
    if s == 0:
        S.union(a, b)
    else:
        if S.find(a) == S.find(b):
            print('YES')
        else:
            print('NO')
class QuickUnion(object):
    def __init__(self, N):
        self.size = [1] * N
        self.array = [i for i in range(N)]

    def root(self, x):
        while x != self.array[x]:
            x = self.array[x]

        return x

    def find(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)
        return root_x == root_y

    def union(self, x, y):
        root_x = self.root(x)
        root_y = self.root(y)

        if self.size[root_x] < self.size[root_y]:
            self.size[root_y] += self.size[root_x]
            self.array[root_x] = root_y
        else:
            self.size[root_x] += self.size[root_y]
            self.array[root_y] = root_x


uf = QuickUnion(10)
uf.union(3, 4)
print(uf.array)
uf.union(4, 9)
print(uf.array)
uf.union(8, 0)
print(uf.array)
uf.union(2, 3)
print(uf.array)
uf.union(5, 6)
print(uf.array)
uf.union(5, 9)
print(uf.array)
uf.union(7, 3)
print(uf.array)
uf.union(4, 8)
print(uf.array)
uf.union(6, 1)
print(uf.array)

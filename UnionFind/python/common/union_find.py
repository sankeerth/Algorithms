class UnionFind(object):
    def __init__(self, size):
        self.size = size
        self.array = [i for i in range(self.size)]

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
        self.array[root_y] = root_x


uf = UnionFind(10)
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

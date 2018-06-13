from collections import defaultdict


class Graph(object):
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_undirected_edge(self, src, dest):
        self.adj_list[src].append(dest)
        self.adj_list[dest].append(src)

    def add_directed_edge(self, src, dest):
        self.adj_list[src].append(dest)
        if not self.adj_list[dest]:
            pass


class GraphWithWeightedEdges(object):
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_undirected_edge(self, src, dest, weight=0):
        self.adj_list[src].append((dest, weight))
        self.adj_list[dest].append((src, weight))

    def add_directed_edge(self, src, dest, weight=0):
        self.adj_list[src].append((dest, weight))
        if not self.adj_list[dest]:
            pass

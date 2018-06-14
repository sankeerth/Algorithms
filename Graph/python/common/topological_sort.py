from Graph.python.common.graph_adj_list import Graph


def topological_sort(graph):
    topological_sorted_nodes = list()
    visited = {node: False for node in graph.adj_list}

    def helper(s):
        visited[s] = True
        for v in graph.adj_list[s]:
            if not visited[v]:
                helper(v)
        topological_sorted_nodes.append(s)

    for node in graph.adj_list.keys():
        if not visited[node]:
            helper(node)

    return topological_sorted_nodes[::-1]


graph = Graph()
graph.add_directed_edge(5, 2)
graph.add_directed_edge(5, 4)
graph.add_directed_edge(4, 0)
graph.add_directed_edge(4, 1)
graph.add_directed_edge(2, 3)
graph.add_directed_edge(3, 1)

print(topological_sort(graph))

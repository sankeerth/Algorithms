from Graph.python.common.graph_adj_list import Graph


def detect_cycle(graph):
    visited = {node: False for node in graph.adj_list}
    parent = {node: -1 for node in graph.adj_list}
    cycle_list = list()

    def detect_cycle_util(s):
        visited[s] = True
        cycle_list.append(s)
        for v in graph.adj_list[s]:
            if not visited[v]:
                parent[v] = s
                detect_cycle_util(v)
            elif parent[s] != v:
                print(cycle_list + [v])
        cycle_list.pop()

    for node in graph.adj_list:
        if not visited[node]:
            detect_cycle_util(node)


graph = Graph()
graph.add_undirected_edge(0, 1)
graph.add_undirected_edge(0, 2)
graph.add_undirected_edge(0, 3)
graph.add_undirected_edge(1, 2)
graph.add_undirected_edge(3, 4)
graph.add_undirected_edge(4, 3)

detect_cycle(graph)

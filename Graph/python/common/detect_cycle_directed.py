from Graph.python.common.graph_adj_list import Graph


def detect_cycle(graph):
    visited = {node: False for node in graph.adj_list}
    cycle_list = list()

    def detect_cycle_util(s):
        visited[s] = True
        stack[s] = True
        cycle_list.append(s)

        for v in graph.adj_list[s]:
            if not stack[v]:
                detect_cycle_util(v)
            else:
                print(cycle_list + [v])
        cycle_list.pop()

    for node in graph.adj_list:
        if not visited[node]:
            stack = {node: False for node in graph.adj_list}
            detect_cycle_util(node)


graph = Graph()
graph.add_directed_edge(0, 1)
graph.add_directed_edge(0, 2)
graph.add_directed_edge(1, 2)
graph.add_directed_edge(2, 0)
graph.add_directed_edge(2, 3)
graph.add_directed_edge(3, 3)

detect_cycle(graph)
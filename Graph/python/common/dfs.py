from Graph.python.common.graph_adj_list import Graph


def dfs(graph, src):
    visited = {node: False for node in graph.adj_list}
    parent = {node: -1 for node in graph.adj_list}
    level = {node: -1 for node in graph.adj_list}
    i = 0

    def dfs_util(s):
        nonlocal i
        visited[s] = True
        i += 1
        level[s] = i
        for v in graph.adj_list[s]:
            if not visited[v]:
                parent[v] = s
                dfs_util(v)
        i -= 1

    visited[src] = True
    level[src] = i
    parent[src] = src
    for v in graph.adj_list[src]:
        if not visited[v]:
            parent[v] = src
            dfs_util(v)

    return visited, parent, level


graph = Graph()
graph.add_directed_edge(0, 1)
graph.add_directed_edge(0, 2)
graph.add_directed_edge(1, 2)
graph.add_directed_edge(2, 0)
graph.add_directed_edge(2, 3)
graph.add_directed_edge(3, 3)
print(dfs(graph, 2))

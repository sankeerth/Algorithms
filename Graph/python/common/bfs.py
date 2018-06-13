from Graph.python.common.graph_adj_list import Graph


def bfs(graph, src):
    queue = list()
    visited = {node: False for node in graph.adj_list}
    level = {node: -1 for node in graph.adj_list}
    parent = {node: -1 for node in graph.adj_list}

    queue.append(src)
    level[src] = 0
    parent[src] = src
    i = 0

    while queue:
        s = queue.pop(0)
        visited[s] = True
        i += 1
        for v in graph.adj_list[s]:
            if not visited[v]:
                queue.append(v)
                parent[v] = s
                level[v] = i

    return visited, parent, level


graph = Graph()
graph.add_directed_edge(0, 1)
graph.add_directed_edge(0, 2)
graph.add_directed_edge(1, 2)
graph.add_directed_edge(2, 0)
graph.add_directed_edge(2, 3)
graph.add_directed_edge(3, 3)
print(bfs(graph, 2))

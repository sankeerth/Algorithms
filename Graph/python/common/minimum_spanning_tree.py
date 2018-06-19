"""
The idea is to maintain two sets of vertices. The first set contains the vertices already included in the MST,
the other set contains the vertices not yet included. At every step, it considers all the edges that connect the
two sets, and picks the minimum weight edge from these edges. After picking the edge, it moves the other endpoint of
the edge to the set containing MST.
A group of edges that connects two set of vertices in a graph is called cut in graph theory. So, at every step of
Prim’s algorithm, we find a cut (of two sets, one contains the vertices already included in MST and other contains rest
of the verices), pick the minimum weight edge from the cut and include this vertex to MST Set (the set that contains
already included vertices).

How does Prim’s Algorithm Work?
The idea behind Prim’s algorithm is simple, a spanning tree means all vertices must be connected.
So the two disjoint subsets (discussed above) of vertices must be connected to make a Spanning Tree.
And they must be connected with the minimum weight edge to make it a Minimum Spanning Tree.

Algorithm
1) Create a set mstSet that keeps track of vertices already included in MST.
2) Assign a key value to all vertices in the input graph. Initialize all key values as INFINITE.
Assign key value as 0 for the first vertex so that it is picked first.
3) While mstSet doesn’t include all vertices
….a) Pick a vertex u which is not there in mstSet and has minimum key value.
….b) Include u to mstSet.
….c) Update key value of all adjacent vertices of u. To update the key values, iterate through all adjacent vertices.
For every adjacent vertex v, if weight of edge u-v is less than the previous key value of v, update the key value as weight of u-v
"""

from Graph.python.common.graph_adj_list import GraphWithWeightedEdges
from heapq import heappop, heappush


def minimum_spanning_tree(graph, src):
    visited = {node: False for node in graph.adj_list}
    distance = {node: float('inf') for node in graph.adj_list}
    parent = {node: node for node in graph.adj_list}
    queue = list()
    distance[src] = 0
    heappush(queue, (0, src))

    while queue:
        top = heappop(queue)
        # print(top)  # it is seen that same node is added to queue multiple times as and when it is updated, however,
        src = top[1]  # that does not affect the answer because the next time it is popped all nodes adjacent to it are already visited
        visited[src] = True  # to restrict heappush to only as many as num of nodes, a queue can be created initially by pushing all the
        for node in graph.adj_list[src]:  # nodes to a list and traverse the same by checking the min value and pop it or have a function like 'decrease_key' for the heap.
            dest, dist = node[0], node[1]
            if not visited[dest] and dist < distance[dest]:
                distance[dest] = dist
                parent[dest] = src
                heappush(queue, (dist, dest))

    return parent, distance


graph = GraphWithWeightedEdges()
graph.add_undirected_edge(0, 1, 4)
graph.add_undirected_edge(0, 7, 8)
graph.add_undirected_edge(1, 2, 8)
graph.add_undirected_edge(1, 7, 11)
graph.add_undirected_edge(2, 3, 7)
graph.add_undirected_edge(2, 5, 4)
graph.add_undirected_edge(2, 8, 2)
graph.add_undirected_edge(3, 4, 9)
graph.add_undirected_edge(3, 5, 14)
graph.add_undirected_edge(4, 5, 10)
graph.add_undirected_edge(5, 6, 2)
graph.add_undirected_edge(6, 7, 1)
graph.add_undirected_edge(6, 8, 6)
graph.add_undirected_edge(7, 8, 7)

print(minimum_spanning_tree(graph, 0))

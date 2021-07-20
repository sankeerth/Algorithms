"""
Dijkstra’s algorithm is very similar to Prim’s algorithm for minimum spanning tree. Like Prim’s MST, we generate a SPT (shortest path tree) with given source as root. 
We maintain two sets, one set contains vertices included in shortest path tree, other set includes vertices not yet included in shortest path tree. 
At every step of the algorithm, we find a vertex which is in the other set (set of not yet included) and has a minimum distance from the source.
Below are the detailed steps used in Dijkstra’s algorithm to find the shortest path from a single source vertex to all other vertices in the given graph. 

Algorithm 
1) Create a set sptSet (shortest path tree set) that keeps track of vertices included in shortest path tree, i.e., whose minimum distance from source is calculated and finalized. Initially, this set is empty. 
2) Assign a distance value to all vertices in the input graph. Initialize all distance values as INFINITE. Assign distance value as 0 for the source vertex so that it is picked first. 
3) While sptSet doesn’t include all vertices 
    a) Pick a vertex u which is not there in sptSet and has minimum distance value. 
    b) Include u to sptSet. 
    c) Update distance value of all adjacent vertices of u. To update the distance values, iterate through all adjacent vertices. 
    For every adjacent vertex v, if sum of distance value of u (from source) and weight of edge u-v, is less than the distance value of v, 
    then update the distance value of v. 
"""
from Graph.python.common.graph_adj_list import GraphWithWeightedEdges
from heapq import heappop, heappush


def dijkstras(graph, src):
    distances, visited, heap = dict(), set(), list()
    for node in graph.adj_list:
        distances[node] = float('inf')

    distances[src] = 0
    heappush(heap, (distances[src], src))

    while heap:
        _, src = heappop(heap)
        visited.add(src)

        for dest, dist in graph.adj_list[src]:
            if dest not in visited and distances[dest] > dist + distances[src]:
                distances[dest] = dist + distances[src]
                heappush(heap, (distances[dest], dest))

    return distances


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

print(dijkstras(graph, 0))

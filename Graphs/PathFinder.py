"""
LeetCode 1971: Find if Path Exists in Graph

There is a bidirectional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a
bidirectional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex
has an edge to itself.

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2

"""
# noinspection PyPep8Naming
from collections import deque as Queue

GraphNode = int
Edge = list[GraphNode]
Graph = list[Edge]


class Solution:
    @staticmethod
    def construct_graph(n: int, edges: list[Edge]) -> Graph:
        adj_matrix = [[0] * n for _ in range(n)]
        for edge in edges:
            r, c = edge
            adj_matrix[r][c] = 1
            adj_matrix[c][r] = 1
        # print(*adj_matrix, sep="\n")
        return adj_matrix

    # noinspection PyPep8Naming
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        return self.optimised(n, edges, source, destination)
        # graph = Solution.construct_graph(n, edges)
        # return self.traverse(graph, source, destination)
        # return self.traverse2(graph, source, destination)

    """
    Trivial approach
    """

    # noinspection PyMethodMayBeStatic
    def traverse(self, graph: Graph, source: GraphNode, destination: GraphNode) -> bool:
        # do breadth first traversal from source
        # if it reaches destination return true instantly
        # else return false at the end
        nodes = len(graph)
        visited: list[bool] = [False] * nodes
        queue: Queue[GraphNode] = Queue(maxlen=nodes)
        queue.append(source)
        visited[source] = True
        while queue:
            node: GraphNode = queue.popleft()
            if node == destination:
                return True
            for neighbour, is_connected in enumerate(graph[node]):
                if visited[neighbour]:
                    continue
                if is_connected:
                    queue.append(neighbour)
                print(queue)
        return False

    """
    improved approach
    """

    # noinspection PyMethodMayBeStatic
    def traverse2(self, graph: Graph, source: GraphNode, destination: GraphNode) -> bool:
        def search(node: GraphNode):
            visited[node] = True
            if node == destination:
                return True

            for neighbour, is_connected in enumerate(graph[node]):
                if visited[neighbour]:
                    continue
                if is_connected:
                    if search(neighbour):
                        return True
            return False

        nodes = len(graph)
        visited: list[bool] = [False] * nodes
        return search(source)

    @staticmethod
    def construct_graph2(n: int, edges: list[Edge]) -> Graph:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        return graph

    """
    optimised approach
    """

    def optimised(self, nodes: int, edges: list[Edge], source: GraphNode, destination: GraphNode) -> bool:
        graph = self.construct_graph2(nodes, edges)

        visited = [False] * nodes
        queue = Queue([source])
        visited[source] = True

        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for neighbour in graph[node]:
                if visited[neighbour]:
                    continue
                queue.append(neighbour)
                visited[neighbour] = True
        return False


if __name__ == '__main__':
    result = Solution().validPath(n=3, edges=[[0, 1], [1, 2], [2, 0]], source=0, destination=2)
    assert result is True
    result = Solution().validPath(n=6, edges=[[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]], source=0, destination=5)
    assert result is False
    result = Solution().validPath(
        10,
        [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]],
        5, 9
    )
    assert result is True

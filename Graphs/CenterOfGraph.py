"""
LeetCode 1791: Find Center of Star Graph

There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one
center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes
ui and vi. Return the center of the given star graph.

Example 1:
Input: edges = [[1,2],[2,3],[4,2]]
Output: 2
Explanation: As shown in the figure above, node 2 is connected to every other node, so 2 is the center.

Example 2:
Input: edges = [[1,2],[5,1],[1,3],[1,4]]
Output: 1
"""

GraphNode = int
Edge = list[GraphNode]
Graph = list[Edge]


class Solution:
    @staticmethod
    def construct_graph(edges: list[Edge]) -> Graph:
        nodes = len(edges) + 1
        graph = [[] for _ in range(nodes)]
        for r, c in edges:
            graph[r - 1].append(c - 1)
            graph[c - 1].append(r - 1)
        print(*graph, sep='\n')
        return graph

    """
    Brute Force, Trivial Approach
    """

    # noinspection PyPep8Naming
    def findCenter1(self, edges: list[Edge]) -> int:
        graph = self.construct_graph(edges)
        for node, edges in enumerate(graph):
            if len(edges) > 1:
                return node + 1
        return 1

    """
    improved approach
    """

    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def findCenter2(self, edges: list[Edge]) -> int:
        edge1, edge2, *rest = edges
        temp: list[int] = edge1 + edge2
        for item in temp:
            if temp.count(item) > 1:
                return item

    """
    Optimised approach
    """

    def findCenter(self, edges: list[Edge]) -> int:
        if edges[0][0] == edges[1][0]:
            return edges[0][0]
        if edges[0][1] == edges[1][0]:
            return edges[0][1]
        return edges[1][1]


if __name__ == '__main__':
    print(Solution().findCenter([[1, 2], [2, 3], [4, 2]]))
    print(Solution().findCenter([[1, 2], [5, 1], [1, 3], [1, 4]]))

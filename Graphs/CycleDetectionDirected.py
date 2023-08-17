"""
Problem Description

Given a directed graph having A nodes. A matrix B of size M x 2 is given which represents the M edges such that there
is an edge directed from node B[i][0] to node B[i][1].

Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

NOTE:

The cycle must contain at least two nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.

Input 1:

 A = 5
 B = [  [1, 2]
        [4, 1]
        [2, 4]
        [3, 4]
        [5, 2]
        [1, 3] ]
Output 1: 1

Input 2:
 A = 5
 B = [  [1, 2]
        [2, 3]
        [3, 4]
        [4, 5] ]
Output: 0
"""
from typing import List
import sys

sys.setrecursionlimit(1002)

GraphNode = int
Edge = List[GraphNode]
Graph = List[Edge]


class Solution:
    visited = []
    graph = []

    # @param nodes : integer
    # @param edges : list of [list of integers]
    # @return an integer
    def construct_graph(self, nodes: int, edges: List[Edge]) -> Graph:
        graph = [[] for _ in range(nodes)]
        for row, col in edges:
            graph[row - 1].append(col - 1)
        return graph

    def is_cyclic(self, node, pathVisited=None) -> bool:
        pathVisited = pathVisited or [False] * len(self.visited)

        if pathVisited[node]:
            return True
        
        
        if self.visited[node]:
            return False

        self.visited[node] = pathVisited[node] = True
        for neighbour in self.graph[node]:
            if self.is_cyclic(neighbour, pathVisited):
                return True
        pathVisited[node] = False
        return False

    def solve(self, nodes: int, edges: List[Edge]) -> int:
        self.graph = self.construct_graph(nodes, edges)
        self.visited = [False] * nodes

        for i in range(nodes):
            if self.visited[i]:
                continue
            if self.is_cyclic(i):
                return 1
        return 0


if __name__ == "__main__":
    result = Solution().solve(5, [[1, 2], [4, 1], [2, 4], [3, 4], [5, 2], [1, 3]])
    print(result)
    result = Solution().solve(5, [[1, 2], [2, 3], [3, 4], [4, 5]])
    print(result)
    result = Solution().solve(
        5, [[1, 2], [1, 3], [2, 3], [1, 4], [4, 3], [4, 5], [3, 5]]
    )
    print(result)

    # 0 -> 1
    # | \  |
    # 3 -> 2 -> 4

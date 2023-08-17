"""

Problem Description

Given an undirected graph having A nodes labelled from 1 to A with M edges given in a form of matrix B of size M x 2 where (B[i][0], B[i][1]) represents two nodes B[i][0] and B[i][1] connected by an edge.

Find whether the graph contains a cycle or not, return 1 if cycle is present else return 0.

NOTE:

The cycle must contain atleast three nodes.
There are no self-loops in the graph.
There are no multiple edges between two nodes.
The graph may or may not be connected.
Nodes are numbered from 1 to A.
Your solution will run on multiple test cases. If you are using global variables make sure to clear them.
"""
from typing import List

Node = int
Edge = List[Node]
Graph = List[Edge]

class Solution:
    graph = []
    visited = []
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def construct_graph(self, nodes, edges) -> None:
        graph = [[] for _ in range(nodes)]
        for r, c in edges:
            r -= 1
            c -= 1
            graph[r].append(c)
            graph[c].append(r)
        self.graph = graph


    def _isCyclic(self, node: int, parent: int) -> bool:
        self.visited[node] = True
        for neighbour in self.graph[node]:
            if not self.visited[neighbour]:
                if self._isCyclic(neighbour, node):
                    return True
            elif neighbour != parent:
                return True
        return False


    def isCyclic(self, node: int) -> bool:
        return self._isCyclic(node, -1)

    def solve(self, nodes, edges) -> int:
        self.construct_graph(nodes, edges)
        self.visited = [False] * nodes
        for node in range(nodes):
            if self.visited[node]:
                continue
            if self.isCyclic(node):
                return 1
        return 0
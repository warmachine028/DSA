package CycleDetectionUndirected;
/*

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

 */

import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
    private ArrayList<ArrayList<Integer>> graph;

    private boolean[] visited;

    private void constructGraph(int nodes, ArrayList<ArrayList<Integer>> edges) {
        graph = new ArrayList<>(nodes);

        for (int i = 0; i < nodes; i++)
            graph.add(new ArrayList<>());

        for (ArrayList<Integer> edge : edges) {
            graph.get(edge.get(0) - 1).add(edge.get(1) - 1);
            graph.get(edge.get(1) - 1).add(edge.get(0) - 1);
        }
    }

    private boolean isCyclic(int node, int parent) {
        visited[node] = true;
        for (int neighbour : graph.get(node)) {
            if (!visited[neighbour]) {
                if (isCyclic(neighbour, node))
                    return true;
            } else if (neighbour != parent)
                return true;
        }
        return false;
    }

    private boolean isCyclic(int node) {
        return isCyclic(node, -1);
    }

    public int solve(int nodes, ArrayList<ArrayList<Integer>> edges) {
        constructGraph(nodes, edges);
        visited = new boolean[nodes];

        for (int node = 0; node < nodes; node++) {
            if (visited[node])
                continue;
            if (isCyclic(node))
                return 1;
        }
        return 0;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        int result = s.solve(2,
                new ArrayList<>(Arrays.asList(new ArrayList<>(Arrays.asList(1, 2)))));
        System.out.println(result); // 0

        result = s.solve(7,
                new ArrayList<>(
                        Arrays.asList(
                                new ArrayList<>(Arrays.asList(1, 2)),
                                new ArrayList<>(Arrays.asList(2, 3)),
                                new ArrayList<>(Arrays.asList(2, 4)),
                                new ArrayList<>(Arrays.asList(2, 5)),
                                new ArrayList<>(Arrays.asList(2, 7)),
                                new ArrayList<>(Arrays.asList(3, 1)),
                                new ArrayList<>(Arrays.asList(4, 6)),
                                new ArrayList<>(Arrays.asList(5, 6)))));
        System.out.println(result); // 1
    }
}

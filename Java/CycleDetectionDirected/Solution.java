package CycleDetectionDirected;
/*
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
            int row = edge.get(0) - 1, col = edge.get(1) - 1;
            graph.get(row).add(col);
        }
    }

    private boolean isCyclic(int node, boolean[] pathVisited) {
        if (pathVisited[node])
            return true;
        if (visited[node])
            return false;
        visited[node] = true;
        pathVisited[node] = true;
        for (int neighbour : graph.get(node)) {
            if (isCyclic(neighbour, pathVisited))
                return true;
        }
        pathVisited[node] = false;
        return false;
    }

    private boolean isCyclic(int node) {
        return isCyclic(node, new boolean[visited.length]);
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
        Solution sol = new Solution();
        ArrayList<ArrayList<Integer>> edges = new ArrayList<>(Arrays.asList(
                new ArrayList<>(Arrays.asList(1, 2)),
                new ArrayList<>(Arrays.asList(1, 3)),
                new ArrayList<>(Arrays.asList(2, 4)),
                new ArrayList<>(Arrays.asList(3, 4)),
                new ArrayList<>(Arrays.asList(4, 1)),
                new ArrayList<>(Arrays.asList(5, 2))));

        sol.solve(5, edges);
    }
}

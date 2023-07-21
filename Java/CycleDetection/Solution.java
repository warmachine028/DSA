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

        for (int i = 0; i < nodes; i++) {
            if (visited[i])
                continue;
            if (isCyclic(i))
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

from Graphs import GraphNode, Graph


def dfs(_graph: Graph) -> None:
    def traverse(root):
        if root in visited:
            return
        visited.add(root)
        print(root.data, end=' -> ')

        for neighbour in root.neighbours:
            traverse(neighbour)

    visited: set[GraphNode] = set()
    for node in _graph.nodes:
        if node not in visited:
            traverse(node)
    print("NULL")


"""

root -> A(1) -- B(2)
         |       |    E(5)
        D(4) -- C(3)

DFS> A -> B -> C -> D -> E

"""
if __name__ == "__main__":
    A = GraphNode(1)
    B = GraphNode(2)
    C = GraphNode(3)
    D = GraphNode(4, A, C)
    E = GraphNode(5)

    A.neighbours = [B, D]
    B.neighbours = [A, C]
    C.neighbours = [B, D]

    dfs(Graph(A, [A, B, C, D, E]))
    dfs(Graph(E, [E]))
    A.neighbours.clear()
    dfs(Graph(A, [A]))

from Graphs import GraphNode, Graph
from datastax.Lists import Queue


def bfs(_graph: Graph) -> None:
    visited: set[GraphNode] = set()
    nodes = _graph.nodes
    for node in nodes:
        if node in visited:
            continue
        queue = Queue(capacity=len(nodes))
        queue.enqueue(node)
        visited.add(node)

        while not queue.is_empty():
            current_node: GraphNode = queue.dequeue()
            print(current_node.data, end=" -> ")
            for neighbour in current_node.neighbours:
                if neighbour not in visited:
                    queue.enqueue(neighbour)
                    visited.add(neighbour)
    print("NULL")


"""

root -> A(1) -- B(2)
        |       |    E(5)
        D(4) -- C(3)
BFS> A -> B -> D -> C -> E
     1    2    4    3    5
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

    graph = Graph(A, [A, B, C, D, E])
    bfs(graph)

    A.neighbours.clear()
    graph = Graph(A, [A])
    bfs(graph)

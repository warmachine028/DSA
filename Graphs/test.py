from Graphs import GraphNode


if __name__ == "__main__":
    A = GraphNode(1)
    B = GraphNode(2)
    C = GraphNode(3)
    D = GraphNode(4)

    A.neighbours = [B, D]
    B.neighbours = [A, C]
    C.neighbours = [B, D]
    D.neighbours = [A, C]

    root = A

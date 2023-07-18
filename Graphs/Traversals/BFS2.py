from datastax.Lists import Queue

GraphNode = list[int]
Graph = list[GraphNode]


def bfs(graph: Graph):
    nodes = len(graph)
    visited: list[bool] = [False] * nodes
    for node, _ in enumerate(graph):
        if visited[node]:
            continue
        queue = Queue(capacity=nodes)
        queue.enqueue(node)
        visited[node] = True
        while not queue.is_empty():
            current_node = queue.dequeue()
            print(current_node + 1, end=" -> ")
            for neighbour, connected in enumerate(graph[node]):
                if visited[neighbour]:
                    continue
                if connected:
                    queue.enqueue(neighbour)
                    visited[neighbour] = True
    print("NULL")


if __name__ == '__main__':
    adj_matrix = [
        [0, 1, 0, 1, 0],  # A -> {B, D}
        [1, 0, 1, 0, 0],  # B -> {A, C}
        [0, 1, 0, 1, 0],  # C -> {B, D]
        [1, 0, 1, 0, 0],  # D -> {A, C}
        [0, 0, 0, 0, 0]  # E -> {}
    ]

    bfs(adj_matrix)  # 1 -> 2 -> 4 -> 3 -> 5
    # adj_matrix = [[1]]  # 1
    # bfs(adj_matrix)

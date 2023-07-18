# DFS Traversal for an adjacency Matrix

GraphNode = list[int]
Graph = list[GraphNode]


def dfs(graph: Graph) -> None:
    def traverse(root: int):
        if visited[root]:
            return
        visited[root] = True
        print(root + 1, end=' -> ')
        for neighbour, connected in enumerate(graph[root]):
            if visited[neighbour]:
                continue
            if connected:
                traverse(neighbour)

    visited: list[bool] = [False] * len(graph)
    for _index, _ in enumerate(graph):
        if not visited[_index]:
            traverse(_index)
    print('NULL')


if __name__ == '__main__':
    adj_matrix = [
        [0, 1, 0, 1, 0],  # A -> {B, D}
        [1, 0, 1, 0, 0],  # B -> {A, C}
        [0, 1, 0, 1, 0],  # C -> {B, D]
        [1, 0, 1, 0, 0],  # D -> {A, C}
        [0, 0, 0, 0, 0]  # E -> {}
    ]

    dfs(adj_matrix)  # 1 -> 2 -> 3 -> 4 -> 5
    adj_matrix = [[1]]  # 1
    dfs(adj_matrix)

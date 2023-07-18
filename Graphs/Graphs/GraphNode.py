from typing import Self


class GraphNode:
    neighbours = []

    def __init__(self, data: int, *neighbours: Self):
        self.data = data
        self.neighbours = neighbours

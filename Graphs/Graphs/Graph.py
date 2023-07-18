from dataclasses import dataclass
from Graphs.GraphNode import GraphNode
from typing import Optional


@dataclass
class Graph:
    root: Optional[GraphNode]
    nodes: list[GraphNode]

from node import Node
from typing import Tuple

class Edge:
    """
    Represents an undirected labeled edge between two nodes.
    """

    def __init__(self, a: Node, b: Node, label: str, weight: float = 0.0):
        self.a = a
        self.b = b
        self.label = label
        self.weight = float(weight) if weight is not None else 0.0

    def __str__(self) -> str:
        return f"Edge(a={self.a}, b={self.b}, label={self.label}, weight={self.weight})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Edge):
            return False
        same_nodes = {self.a, self.b} == {value.a, value.b}
        return same_nodes and self.label == value.label and self.weight == value.weight

    def __hash__(self) -> int:
        return hash((frozenset({self.a, self.b}), self.label, self.weight))

    def get_nodes(self) -> Tuple[Node, Node]:
        return (self.a, self.b)

    def get_weight(self) -> float:
        return self.weight

    def set_weight(self, weight: float) -> None:
        self.weight = float(weight)

    def get_label(self) -> str:
        return self.label

    def set_label(self, label: str) -> None:
        self.label = label
